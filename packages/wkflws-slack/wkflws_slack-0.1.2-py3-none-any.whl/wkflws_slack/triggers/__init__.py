"""Triggers for Slack."""
import json
from typing import Any, Optional

from wkflws.events import Event
from wkflws.http import http_method, Request, Response
from wkflws.logging import getLogger
from wkflws.triggers.webhook import status, WebhookTrigger

from .. import __identifier__, __version__

logger = getLogger("wkflws_slack.triggers.webhook")
logger.setLevel(10)


async def process_webhook_request(
    request: Request,
    response: Response,
) -> Optional[Event]:
    """Accept and process an HTTP request returning a event for the bus."""
    data = json.loads(request.body)

    # When you first enter a webhook url, slack sends a POST with a challenge. This
    # challenge must be sent back for the webhook to be active.
    if "type" in data and data["type"] == "url_verification":
        # The url_verification has nothing to process.
        response.status_code = status.HTTP_200_OK
        response.headers = {
            "Content-Type": "text/plain",
        }
        response.body = data["challenge"]

        logger.info(f'Unique token: {data["token"]}')

        return None

    metadata = request.headers.copy()
    metadata["webhook_token"] = data["token"]

    identifier = data["event_id"]

    logger.info(f"Received Slack webhook request {identifier}")

    # 3. Finally return the Event with as little modification to the data as possible.
    return Event(identifier, metadata, data)


async def accept_event(event: Event) -> tuple[Optional[str], dict[str, Any]]:
    """Accept and process data from the event bus."""
    data = event.data

    event_type = data["event"]["type"]

    logger.info(f"Processing Slack webhook as '{event_type}' event")
    match event_type:
        case "message":
            return "wkflws_slack.triggers.receive_message", data
        case _:
            logger.error(
                f"Received unsupported github event type '{event_type}' "
                f"(id:{event.identifier})"
            )
            return None, {}


webhook = WebhookTrigger(
    client_identifier=__identifier__,
    client_version=__version__,
    process_func=accept_event,
    routes=(
        (
            (http_method.POST,),
            "/slack/webhook/",
            process_webhook_request,
        ),
    ),
)

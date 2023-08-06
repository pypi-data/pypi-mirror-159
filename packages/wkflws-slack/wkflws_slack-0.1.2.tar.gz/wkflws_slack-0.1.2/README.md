# wkflws_slack
This node provides functionality for interacting with Slack instances as a bot.

## Context Properities
The following context properties are required for this node.
| name | description |
|-|-|
| `slack_bot_token` | Slack bot token (starts with xoxb-). Obtain from [here](https://api.slack.com/apps). |

## wkflws_slack.triggers.receive_message

This is a trigger node that processes a message from Slack. To set this up use the
[Event Subscriptions](https://api.slack.com/apis/connections/events-api) feature of Slack.

## Example Output

```json
{
  "token": "your_unique_token",
  "team_id": "T7V82H94",
  "api_app_id": "A03J4B7042",
  "event": {
    "client_msg_id": "096b65e2-5d17-44b8-9968-fd3344c60e4e",
    "type": "message",
    "text": "Did you get that thing I sent you?",
    "user": "U02OD4PJQ91",
    "ts": "1658257879.109959",
    "team": "T7V82H94",
    "blocks": [
      {
        "type": "rich_text",
        "block_id": "fsa",
        "elements": [
          {
            "type": "rich_text_section",
            "elements": [
              {
                "type": "text",
                "text": "Did you get that thing I sent you?"
              }
            ]
          }
        ]
      }
    ],
    "channel": "D08MP7R81K7",
    "event_ts": "1658257879.109959",
    "channel_type": "im"
  },
  "type": "event_callback",
  "event_id": "Ev03MZAIM942",
  "event_time": 1658257879,
  "authorizations": [
    {
      "enterprise_id": null,
      "team_id": "T7V82H94",
      "user_id": "U03K7QIM9C",
      "is_bot": true,
      "is_enterprise_install": false
    }
  ],
  "is_ext_shared_channel": false,
  "event_context": "4-eyJ..In0"
}
```

## wkflws_slack.send_message

This is an action node which sends a message to a Slack channel as a bot user.

## Parameters
The following parameters are available.
| name | required | description |
|-|-|-|
| `channel`| ✅ | The channel, DM, or MPIM id to send the message to. |
| `message`| ✅ | The (raw text) message to send. |
| `username` | ❌  | The username to send the message as. *Defaults to the bot's name*. |
| `icon_emoji` | ❌  | An emoji to use as the bot's icon. |
| `icon_url` | ❌  | URL to an Image to use as the bot's icon. |

## Example Input

```json
{
  "channel": "C08MP7R81K7",
  "message": "No, try resending."
}
```

## Example Output
```json
{
  "ok": true,
  "channel": "D08MP7R81K7",
  "ts": "1658258988.263199",
  "message": {
    "bot_id": "B03KM33M17F",
    "type": "message",
    "text": "No, try resending.",
    "user": "U03K7QIM9C",
    "ts": "1658258988.263199",
    "app_id": "A03J4B7042",
    "team": "T7V82H94",
    "bot_profile": {
      "id": "B03KM33M17F",
      "app_id": "A03J4B7042",
      "name": "George",
      "icons": {
        "image_36": "https://avatars.slack-edge.com/2022-06-13/3647926278103_b51dccf308a7ae82234e_36.png",
        "image_48": "https://avatars.slack-edge.com/2022-06-13/3647926278103_b51dccf308a7ae82234e_48.png",
        "image_72": "https://avatars.slack-edge.com/2022-06-13/3647926278103_b51dccf308a7ae82234e_72.png"
      },
      "deleted": false,
      "updated": 1655160233,
      "team_id": "T7V82H94"
    },
    "blocks": [
      {
        "type": "rich_text",
        "block_id": "6Ag+",
        "elements": [
          {
            "type": "rich_text_section",
            "elements": [
              {
                "type": "text",
                "text": "No, try resending."
              }
            ]
          }
        ]
      }
    ]
  }
}
```

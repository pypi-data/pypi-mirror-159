# Sync-Ends


[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) ![GitHub](https://img.shields.io/badge/language-python-blue.svg) [![Build Status](https://travis-ci.com/jaymodi98/Sync-Ends.svg?branch=master)](https://travis-ci.com/jaymodi98/Sync-Ends)
<br>![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/jaymodi98/Sync-Ends) ![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/jaymodi98/Sync-Ends) ![codecov](https://codecov.io/gh/jaymodi98/Sync-Ends/branch/master/graph/badge.svg?token=DP2AWTXOXL)
<br>![YouTube Video Views](https://img.shields.io/youtube/views/1Pd3Enj13m8?style=social)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture Diagram](#architecture-diagram)
- [How to Setup](#how-to-setup)
- [Config file Setup](#config-file-setup)
- [Prerequisites](#prerequisites)
  * [Step 1: Setup Postman](#step-1-setup-postman)
  * [Step 2: Create a Slack workspace and integrate Slack bot](#step-2-create-a-slack-workspace-and-integrate-slack-bot)
    + [2a. Creating Slack workspace](#2a-creating-slack-workspace)
    + [2b. Creating Slack bot](#2b-creating-slack-bot)
- [Code Documentation](#code-documentation)
- [License](#license)

## Overview

Sync-Ends is a productivity service, an automated bridge to sync service owners and service consumers that focuses on saving developer time by automatically notifying API consumers when a change is made in the API.

With more and more teams working autonomously and focusing on a microservice and API-driven culture, it is a hassle, for the API developers to keep notifying their consumers of API changes, and for the API consumers to keep track of these API changes and make required changes in their codebase.

Sync-Ends service addresses this problem by taking the hassle away from the API developers and consumers. The Sync-Ends service continuously monitors the API collection in Postman (being worked on by API developers) and every time an API changes in this collection, it notifies a slack channel (followed by the API consumers) with a diff of the change. This way, API developers don't need to manually post messages every time something changes in the service and API consumers are sure that they are utilising the latest API changes.

Take a look at this short video to understand the project idea better.
[![Watch the video](images/screenshotpromo.png)](https://www.youtube.com/watch?v=1Pd3Enj13m8)

## Features
|Feature|Description  |
|--|--|
|1-step service execution |```Simple 1-step CLI execution for Sync Ends service```|
|API Change Notification  |```Get notifications about changes made to the API in Postman along with detailed diff of changes```|
|Track Postman collection | ```Ability to track a Postman collection and get notifications```|
|Slack Bot Subscription   |``` Set frequency of notifications as well as customize Slack channel for updates``` |

## Architecture Diagram
<img src="images/architecture.PNG" height="500" width="800"/>

## How to Setup

1. Perform the steps described in the [Prerequisites](#prerequisites) section.
2. Install python 3.
3. To install packages, run: `pip install -r requirements.txt`
4. Create a config json file to be used by the Sync Ends service. Refer to the [config file setup section](#config-file-setup) for details.
5. Run the service using: `python src/main.py --config <config-file-path>`

## Config file Setup
The _sync-ends_ service uses a configuration file to configure postman token, slack channels and other parameters required to run the service. The file format must be `.json`. Here's how the config file looks like:
```
{
    "postman_api_key": "<a>",
    "slack_token": "<b>",
    "trigger_interval": <c>,
    "collections": [
        {
            "collection_name": "<d>",
            "slack_channel": "<e>"
        }
    ]
}
```
where,
- `a`: postman api key generated using steps shown in [Postman Setup section](#step-1-setup-postman).
- `b`: slack token generated using steps shown in [Slack Setup section](#step-2-create-a-slack-workspace-and-integrate-slack-bot).
- `c`: _[optional: default=10]_ time (in seconds), after which application will periodically check for api changes
- `d`: collection name from postman collections
- `e`: _[optional: default="general"]_ slack channel in which notifications will be sent (must be a public channel)

## Prerequisites

### Step 1: Setup Postman
1. Sign in to [Postman](https://identity.getpostman.com/login).
2. If you do not have any pre-exiting collections on Postman, import this [sample collection](https://www.postman.com/collections/e2cb1b9c870ee78fc20d).
3. To integrate with the Sync Ends service, a Postman API key is required. Generate API key by visiting this [page](https://web.postman.co/settings/me/api-keys).
4. Copy the generated API key. This is required during the time of execution of the service. Make sure you store it safely as you won't be able to view this any other time.

### Step 2: Create a Slack workspace and integrate Slack bot

#### 2a. Creating Slack workspace
1. Open https://slack.com/.
2. Provide your email ID. Select `Create New workspace`.
3. Check your email and enter the code to verify your email.
4. Provide your name and set a password.
5. Add some details to your workspace in the next page.
6. Provide a company name.
7. Workspace URL should be unique. Also remember this URL, this is what is used to login to your Slack instance.
8. Agree with the terms.
9. Skip the invite step.
10. You are up and running with your own instance of Slack.

#### 2b. Creating Slack bot
1. Open your `<workspace-URL>/apps` (the one you created above). For example, [https://test-visual.slack.com/apps](https://test-visual.slack.com/apps).
2. Search for bot in the search bar and select `Bots`.
3. In the Bots landing page, click on `Add configuration`.
4. Provide a Bot name. For example, `wolfpack-bot` and click on `Add Bot integration`.
5. In the `Setup instruction` page: `Copy and store the API Token`. For example, the token may look something like this: `xoxb-22672546-n1X9APk3D0tfksr81NJj6VAM`.
6. Save the Bot integration.

## Code Documentation
The documentation for the code classes and methods is generated using `pdoc3`. To view this documentation, clone the repo and navigate to `docs/src/` and open `index.html` in a browser.

## License

This project is licensed under the MIT License.

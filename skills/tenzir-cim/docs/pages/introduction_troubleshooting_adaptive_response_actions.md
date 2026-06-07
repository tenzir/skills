---
title: Troubleshooting adaptive response actions
url: https://help.splunk.com/en/data-management/common-information-model/8.5/introduction/troubleshooting-adaptive-response-actions
last_modified: 2026-04-01T20:48:27.998Z
version: 8.5
---

# Troubleshooting adaptive response actions

Following are some issues that you might see when configuring adaptive response relay actions:

## Issue: Troubleshoot adaptive response actions in search head cluster deployments on Splunk Cloud Platform

The adaptive response framework displays error messages on Splunk Cloud Platform (SCP) search head cluster (SHC) deployments when using Common Information model (CIM) Add-on versions 5.0.2 and lower. Errors occur on Splunk Cloud Platform deployments using the CIM Add-on and Splunk Enterprise Security deployments that bundle the CIM Add-on.

If you are a Splunk Cloud Platform customer, you can configure your Splunk Cloud Platform Enterprise Security search head with an API key, which allows you to authenticate from the KV Store collection and Common Action Model (CAM) queue. The CAM adaptive response relay worker is installed on-prem and configured to communicate with Splunk Cloud Platform using the Common Information Model. For more information, see Configure your Splunk Cloud Platform ES search head with an API key .

The on-prem CAM relay worker runs every 60 seconds on the Splunk Cloud Platform CAM queue and checks whether an alert action exists in the queue or not. if an alert action exists in the CAM queue, the CAM relay worker runs the alert action. The adaptive response framework displays "500 Server Error" messages when connecting to Splunk Cloud from the on-prem CAM relay worker.

For example:

`2022-07-15 09:52:59,874+0000 ERROR pid=16227 tid=MainThread file=relaymodaction.py:run:328 | Failed to fetch results: 500 Server Error: Internal Server Error for url: https://customer-gsoc.splunkcloud.com:8089/services/alerts/modaction_queue/peek/LOG-HF09.mycustomer.com@@cff33f3c137b6af7faecc825381fdeb73841964d `

Adaptive response action errors cause a delay between the time when the alert is sent to the queue and the time when the on-prem CAM relay worker dequeues the alert. For example, If an on-prem CAM relay worker tries to connect to Splunk Cloud every 60 seconds and there is an 18 minute delay, , this implies that the CAM relay worker can connect to Splunk Cloud Platform successfully only after 18 attempts.

The following architectural diagram depicts the process workflow for adaptive response actions in a search head cluster deployment on Splunk Cloud Platform:

## Cause

By default, configuring the adaptive response relay (ARR) framework is supported on Splunk Cloud Platform deployments that have Splunk Enterprise Security.

## Solution

Install and configure the following apps manually to configure the adaptive response relay (ARR) framework on deployments that do not have Splunk Enterprise Security.

- Splunk_SA_CIM
- Splunk_TA_AROnPrem
- Splunk_TA_ForIndexers

For more information on configuring an adaptive response relay and the apps, see Set up an Adaptive Response relay from a Splunk Cloud Platform Enterprise Security search head to an on-premises device .

Retrieve these app packages from an existing Splunk Enterprise Security installation as a .tar or .zip file and install it on the search head. You must have access to both deployments to install the apps.

If you do not have access to an ES deployment, you can install and configure the app on an on-prem test deployment using the app manager UI. Installing the apps on an on-prem deployment ensures that all *.csv.default lookup files are enabled. After the CIM app is installed, you can install the pre-configured app package to the search head on a Cloud deployment.

## Issue: Troubleshoot configuring adaptive response actions in deployments that do not have Splunk Enterprise Security

Configuring the adaptive response relay (ARR) framework in deployments that do not have Splunk Enterprise Security installed might require some additional configuration steps.

## Cause

By default, configuring the adaptive response relay (ARR) framework is supported on Splunk Cloud Platform deployments that have Splunk Enterprise Security.

## Solution

Install and configure the following apps manually to configure the adaptive response relay (ARR) framework on deployments that do not have Splunk Enterprise Security.

- Splunk_SA_CIM
- Splunk_TA_AROnPrem
- Splunk_TA_ForIndexers

For more information on configuring an adaptive response relay and the apps, see Set up an Adaptive Response relay from a Splunk Cloud Platform Enterprise Security search head to an on-premises device .

Retrieve these app packages from an existing Splunk Enterprise Security installation as a .tar or .zip file and install it on the search head. You must have access to both deployments to install the apps.

If you do not have access to an ES deployment, you can install and configure the app on an on-prem test deployment using the app manager UI. Installing the apps on an on-prem deployment ensures that all *.csv.default lookup files are enabled. After the CIM app is installed, you can install the pre-configured app package to the search head on a Cloud deployment.

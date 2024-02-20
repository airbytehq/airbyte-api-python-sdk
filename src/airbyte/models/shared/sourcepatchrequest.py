"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .source_aha import SourceAha
from .source_aircall import SourceAircall
from .source_airtable import SourceAirtable
from .source_amazon_ads import SourceAmazonAds
from .source_amazon_seller_partner import SourceAmazonSellerPartner
from .source_amazon_sqs import SourceAmazonSqs
from .source_amplitude import SourceAmplitude
from .source_apify_dataset import SourceApifyDataset
from .source_appfollow import SourceAppfollow
from .source_asana import SourceAsana
from .source_auth0 import SourceAuth0
from .source_aws_cloudtrail import SourceAwsCloudtrail
from .source_azure_blob_storage import SourceAzureBlobStorage
from .source_azure_table import SourceAzureTable
from .source_bamboo_hr import SourceBambooHr
from .source_bigquery import SourceBigquery
from .source_bing_ads import SourceBingAds
from .source_braintree import SourceBraintree
from .source_braze import SourceBraze
from .source_cart import SourceCart
from .source_chargebee import SourceChargebee
from .source_chartmogul import SourceChartmogul
from .source_clickhouse import SourceClickhouse
from .source_clickup_api import SourceClickupAPI
from .source_clockify import SourceClockify
from .source_close_com import SourceCloseCom
from .source_coda import SourceCoda
from .source_coin_api import SourceCoinAPI
from .source_coinmarketcap import SourceCoinmarketcap
from .source_configcat import SourceConfigcat
from .source_confluence import SourceConfluence
from .source_convex import SourceConvex
from .source_datascope import SourceDatascope
from .source_delighted import SourceDelighted
from .source_dixa import SourceDixa
from .source_dockerhub import SourceDockerhub
from .source_dremio import SourceDremio
from .source_dynamodb import SourceDynamodb
from .source_e2e_test_cloud import ContinuousFeed
from .source_emailoctopus import SourceEmailoctopus
from .source_exchange_rates import SourceExchangeRates
from .source_facebook_marketing import SourceFacebookMarketing
from .source_faker import SourceFaker
from .source_fauna import SourceFauna
from .source_file import SourceFile
from .source_firebolt import SourceFirebolt
from .source_freshcaller import SourceFreshcaller
from .source_freshdesk import SourceFreshdesk
from .source_freshsales import SourceFreshsales
from .source_gainsight_px import SourceGainsightPx
from .source_gcs import SourceGcs
from .source_getlago import SourceGetlago
from .source_github import SourceGithub
from .source_gitlab import SourceGitlab
from .source_glassfrog import SourceGlassfrog
from .source_gnews import SourceGnews
from .source_google_ads import SourceGoogleAds
from .source_google_analytics_data_api import SourceGoogleAnalyticsDataAPI
from .source_google_analytics_v4_service_account_only import SourceGoogleAnalyticsV4ServiceAccountOnly
from .source_google_directory import SourceGoogleDirectory
from .source_google_drive import SourceGoogleDrive
from .source_google_pagespeed_insights import SourceGooglePagespeedInsights
from .source_google_search_console import SourceGoogleSearchConsole
from .source_google_sheets import SourceGoogleSheets
from .source_google_webfonts import SourceGoogleWebfonts
from .source_google_workspace_admin_reports import SourceGoogleWorkspaceAdminReports
from .source_greenhouse import SourceGreenhouse
from .source_gridly import SourceGridly
from .source_harvest import SourceHarvest
from .source_hubplanner import SourceHubplanner
from .source_hubspot import SourceHubspot
from .source_insightly import SourceInsightly
from .source_instagram import SourceInstagram
from .source_instatus import SourceInstatus
from .source_intercom import SourceIntercom
from .source_ip2whois import SourceIp2whois
from .source_iterable import SourceIterable
from .source_jira import SourceJira
from .source_k6_cloud import SourceK6Cloud
from .source_klarna import SourceKlarna
from .source_klaviyo import SourceKlaviyo
from .source_kyve import SourceKyve
from .source_launchdarkly import SourceLaunchdarkly
from .source_lemlist import SourceLemlist
from .source_lever_hiring import SourceLeverHiring
from .source_linkedin_ads import SourceLinkedinAds
from .source_linkedin_pages import SourceLinkedinPages
from .source_lokalise import SourceLokalise
from .source_mailchimp import SourceMailchimp
from .source_mailgun import SourceMailgun
from .source_mailjet_sms import SourceMailjetSms
from .source_marketo import SourceMarketo
from .source_metabase import SourceMetabase
from .source_microsoft_sharepoint import SourceMicrosoftSharepoint
from .source_microsoft_teams import SourceMicrosoftTeams
from .source_mixpanel import SourceMixpanel
from .source_monday import SourceMonday
from .source_mongodb_internal_poc import SourceMongodbInternalPoc
from .source_mongodb_v2 import SourceMongodbV2
from .source_mssql import SourceMssql
from .source_my_hours import SourceMyHours
from .source_mysql import SourceMysql
from .source_netsuite import SourceNetsuite
from .source_notion import SourceNotion
from .source_nytimes import SourceNytimes
from .source_okta import SourceOkta
from .source_omnisend import SourceOmnisend
from .source_onesignal import SourceOnesignal
from .source_oracle import SourceOracle
from .source_orb import SourceOrb
from .source_orbit import SourceOrbit
from .source_outbrain_amplify import SourceOutbrainAmplify
from .source_outreach import SourceOutreach
from .source_paypal_transaction import SourcePaypalTransaction
from .source_paystack import SourcePaystack
from .source_pendo import SourcePendo
from .source_persistiq import SourcePersistiq
from .source_pexels_api import SourcePexelsAPI
from .source_pinterest import SourcePinterest
from .source_pipedrive import SourcePipedrive
from .source_pocket import SourcePocket
from .source_pokeapi import SourcePokeapi
from .source_polygon_stock_api import SourcePolygonStockAPI
from .source_postgres import SourcePostgres
from .source_posthog import SourcePosthog
from .source_postmarkapp import SourcePostmarkapp
from .source_prestashop import SourcePrestashop
from .source_punk_api import SourcePunkAPI
from .source_pypi import SourcePypi
from .source_qualaroo import SourceQualaroo
from .source_quickbooks import SourceQuickbooks
from .source_railz import SourceRailz
from .source_recharge import SourceRecharge
from .source_recreation import SourceRecreation
from .source_recruitee import SourceRecruitee
from .source_redshift import SourceRedshift
from .source_retently import SourceRetently
from .source_rki_covid import SourceRkiCovid
from .source_rss import SourceRss
from .source_s3 import SourceS3
from .source_salesforce import SourceSalesforce
from .source_salesloft import SourceSalesloft
from .source_sap_fieldglass import SourceSapFieldglass
from .source_secoda import SourceSecoda
from .source_sendgrid import SourceSendgrid
from .source_sendinblue import SourceSendinblue
from .source_senseforce import SourceSenseforce
from .source_sentry import SourceSentry
from .source_sftp import SourceSftp
from .source_sftp_bulk import SourceSftpBulk
from .source_shopify import SourceShopify
from .source_shortio import SourceShortio
from .source_slack import SourceSlack
from .source_smaily import SourceSmaily
from .source_smartengage import SourceSmartengage
from .source_smartsheets import SourceSmartsheets
from .source_snapchat_marketing import SourceSnapchatMarketing
from .source_snowflake import SourceSnowflake
from .source_sonar_cloud import SourceSonarCloud
from .source_spacex_api import SourceSpacexAPI
from .source_square import SourceSquare
from .source_strava import SourceStrava
from .source_stripe import SourceStripe
from .source_survey_sparrow import SourceSurveySparrow
from .source_surveymonkey import SourceSurveymonkey
from .source_tempo import SourceTempo
from .source_the_guardian_api import SourceTheGuardianAPI
from .source_tiktok_marketing import SourceTiktokMarketing
from .source_trello import SourceTrello
from .source_trustpilot import SourceTrustpilot
from .source_tvmaze_schedule import SourceTvmazeSchedule
from .source_twilio import SourceTwilio
from .source_twilio_taskrouter import SourceTwilioTaskrouter
from .source_twitter import SourceTwitter
from .source_typeform import SourceTypeform
from .source_us_census import SourceUsCensus
from .source_vantage import SourceVantage
from .source_webflow import SourceWebflow
from .source_whisky_hunter import SourceWhiskyHunter
from .source_wikipedia_pageviews import SourceWikipediaPageviews
from .source_woocommerce import SourceWoocommerce
from .source_xkcd import SourceXkcd
from .source_yandex_metrica import SourceYandexMetrica
from .source_yotpo import SourceYotpo
from .source_youtube_analytics import SourceYoutubeAnalytics
from .source_zendesk_chat import SourceZendeskChat
from .source_zendesk_sell import SourceZendeskSell
from .source_zendesk_sunshine import SourceZendeskSunshine
from .source_zendesk_support import SourceZendeskSupport
from .source_zendesk_talk import SourceZendeskTalk
from .source_zenloop import SourceZenloop
from .source_zoho_crm import SourceZohoCrm
from .source_zoom import SourceZoom
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePatchRequest:
    configuration: Optional[Union[SourceAha, SourceAircall, SourceAirtable, SourceAmazonAds, SourceAmazonSellerPartner, SourceAmazonSqs, SourceAmplitude, SourceApifyDataset, SourceAppfollow, SourceAsana, SourceAuth0, SourceAwsCloudtrail, SourceAzureBlobStorage, SourceAzureTable, SourceBambooHr, SourceBigquery, SourceBingAds, SourceBraintree, SourceBraze, SourceCart, SourceChargebee, SourceChartmogul, SourceClickhouse, SourceClickupAPI, SourceClockify, SourceCloseCom, SourceCoda, SourceCoinAPI, SourceCoinmarketcap, SourceConfigcat, SourceConfluence, SourceConvex, SourceDatascope, SourceDelighted, SourceDixa, SourceDockerhub, SourceDremio, SourceDynamodb, Union[ContinuousFeed], SourceEmailoctopus, SourceExchangeRates, SourceFacebookMarketing, SourceFaker, SourceFauna, SourceFile, SourceFirebolt, SourceFreshcaller, SourceFreshdesk, SourceFreshsales, SourceGainsightPx, SourceGcs, SourceGetlago, SourceGithub, SourceGitlab, SourceGlassfrog, SourceGnews, SourceGoogleAds, SourceGoogleAnalyticsDataAPI, SourceGoogleAnalyticsV4ServiceAccountOnly, SourceGoogleDirectory, SourceGoogleDrive, SourceGooglePagespeedInsights, SourceGoogleSearchConsole, SourceGoogleSheets, SourceGoogleWebfonts, SourceGoogleWorkspaceAdminReports, SourceGreenhouse, SourceGridly, SourceHarvest, SourceHubplanner, SourceHubspot, SourceInsightly, SourceInstagram, SourceInstatus, SourceIntercom, SourceIp2whois, SourceIterable, SourceJira, SourceK6Cloud, SourceKlarna, SourceKlaviyo, SourceKyve, SourceLaunchdarkly, SourceLemlist, SourceLeverHiring, SourceLinkedinAds, SourceLinkedinPages, SourceLokalise, SourceMailchimp, SourceMailgun, SourceMailjetSms, SourceMarketo, SourceMetabase, SourceMicrosoftSharepoint, SourceMicrosoftTeams, SourceMixpanel, SourceMonday, SourceMongodbInternalPoc, SourceMongodbV2, SourceMssql, SourceMyHours, SourceMysql, SourceNetsuite, SourceNotion, SourceNytimes, SourceOkta, SourceOmnisend, SourceOnesignal, SourceOracle, SourceOrb, SourceOrbit, SourceOutbrainAmplify, SourceOutreach, SourcePaypalTransaction, SourcePaystack, SourcePendo, SourcePersistiq, SourcePexelsAPI, SourcePinterest, SourcePipedrive, SourcePocket, SourcePokeapi, SourcePolygonStockAPI, SourcePostgres, SourcePosthog, SourcePostmarkapp, SourcePrestashop, SourcePunkAPI, SourcePypi, SourceQualaroo, SourceQuickbooks, SourceRailz, SourceRecharge, SourceRecreation, SourceRecruitee, SourceRedshift, SourceRetently, SourceRkiCovid, SourceRss, SourceS3, SourceSalesforce, SourceSalesloft, SourceSapFieldglass, SourceSecoda, SourceSendgrid, SourceSendinblue, SourceSenseforce, SourceSentry, SourceSftp, SourceSftpBulk, SourceShopify, SourceShortio, SourceSlack, SourceSmaily, SourceSmartengage, SourceSmartsheets, SourceSnapchatMarketing, SourceSnowflake, SourceSonarCloud, SourceSpacexAPI, SourceSquare, SourceStrava, SourceStripe, SourceSurveySparrow, SourceSurveymonkey, SourceTempo, SourceTheGuardianAPI, SourceTiktokMarketing, SourceTrello, SourceTrustpilot, SourceTvmazeSchedule, SourceTwilio, SourceTwilioTaskrouter, SourceTwitter, SourceTypeform, SourceUsCensus, SourceVantage, SourceWebflow, SourceWhiskyHunter, SourceWikipediaPageviews, SourceWoocommerce, SourceXkcd, SourceYandexMetrica, SourceYotpo, SourceYoutubeAnalytics, SourceZendeskChat, SourceZendeskSell, SourceZendeskSunshine, SourceZendeskSupport, SourceZendeskTalk, SourceZenloop, SourceZohoCrm, SourceZoom]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration'), 'exclude': lambda f: f is None }})
    r"""The values required to configure the source."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    secret_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secretId'), 'exclude': lambda f: f is None }})
    r"""Optional secretID obtained through the public API OAuth redirect flow."""
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId'), 'exclude': lambda f: f is None }})
    


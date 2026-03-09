# Tenzir Platform

> The control plane for managing Tenzir Nodes, providing a web interface for data exploration and pipeline creation, and workspace and secret management.


The control plane for managing Tenzir Nodes, providing a web interface for data exploration and pipeline creation, and workspace and secret management.

[ GitHub ](https://github.com/tenzir/platform/releases)

[Download releases and artifacts](https://github.com/tenzir/platform/releases)

[ RSS Feed ](/changelog/platform.xml)

[Subscribe to release updates](/changelog/platform.xml)

## Releases

* [v1.29.0 Mar 5, 2026](platform/v1-29-0.md)

  [With this release, the Tenzir Platform preserves deep links through the login flow, so users are redirected to their original destination after signing in. It also includes several bug fixes and a performance improvement for loading across the platform.](platform/v1-29-0.md)
* [v1.28.3 Feb 24, 2026](platform/v1-28-3.md)

  [This release improves the clarity and usability of Explorer charts with better legends, tooltips, and an expanded color palette. It also fixes several UI bugs including unresponsive pipeline lists and stale workspace cleanup.](platform/v1-28-3.md)
* [v1.28.2 Feb 17, 2026](platform/v1-28-2.md)

  [This release brings the Platform's dependencies up to date with the latest CVE fixes.](platform/v1-28-2.md)
* [v1.28.1 Feb 10, 2026](platform/v1-28-1.md)

  [This release upgrades pnpm to 9.15.0 in the frontend Docker image to address CVE-2024-53866.](platform/v1-28-1.md)
* [v1.28.0 Feb 9, 2026](platform/v1-28-0.md)

  [This release unifies the library's Available and Installed tabs into a single view, making package management more streamlined. It also adds pipeline activity sorting, series isolation in activity charts, a line wrap toggle in the Inspector, platform version display, and a backslash escaping fix.](platform/v1-28-0.md)
* [v1.27.1 Feb 2, 2026](platform/v1-27-1.md)

  [This release fixes a bug where users could experience authentication failures due to stale user keys in their session. The platform now proactively checks for expired keys and refreshes them automatically.](platform/v1-27-1.md)
* [v1.27.0 Jan 26, 2026](platform/v1-27-0.md)

  [This release improves the pipeline detail view with faster loading and a convenient close button for quick navigation. Error messages are now cleaner with collapsible technical details, and we fixed issues where the UI could hang or become unresponsive. This release also includes security hardeni...](platform/v1-27-0.md)
* [v1.26.0 Dec 23, 2025](platform/v1-26-0.md)

  [This release adds HashiCorp Vault as an external secret store for workspaces. The integration supports token and AppRole authentication with the KV v2 secrets engine.](platform/v1-26-0.md)
* [v1.25.1 Dec 16, 2025](platform/v1-25-1.md)

  [This patch release fixes an issue with default filesystem paths in the Tenzir Platform docker containers for Sovereign Edition users.](platform/v1-25-1.md)
* [v1.25.0 Dec 15, 2025](platform/v1-25-0.md)

  [This release includes some UI fixes and minor improvements to smooth out common workflows. We fixed incorrect rendering of negative durations, resolved an issue where the node selector reset during navigation, and addressed a layout issue that could hide the install button in the package drawer.](platform/v1-25-0.md)
* [v1.24.0 Dec 10, 2025](platform/v1-24-0.md)

  [This release includes many small UI fixes, as well as new TLS options for the websocket gateway.](platform/v1-24-0.md)
* [v1.23.1 Nov 24, 2025](platform/v1-23-1.md)

  [We fixed an issue where dashboard cells without a fixed node ID sometimes failed to render. These cells now render correctly using sensible fallbacks.](platform/v1-23-1.md)
* [v1.23.0 Nov 20, 2025](platform/v1-23-0.md)

  [The seaweedfs service in our example setups now runs as non-root user and automatically adds the correct CORS headers. Be sure to read the \\"Changes\\" section below if you're using it in a self-hosted environment. As always, a slew of frontend improvements are included in this release as well.](platform/v1-23-0.md)
* [v1.22.0 Nov 13, 2025](platform/v1-22-0.md)

  [This release includes a variety of UI improvements and bugfixes, as well as a new configuration option for working with external OIDC providers.](platform/v1-22-0.md)
* [v1.21.0 Nov 3, 2025](platform/v1-21-0.md)

  [This release improves how you browse, edit, and share pipelines. We fixed overlapping timestamps in the activity chart, made pipeline updates more reliable and visible, sped up library loading, and added a new button in the editor to copy a link to the current pipeline.](platform/v1-21-0.md)
* [v1.20.0 Oct 22, 2025](platform/v1-20-0.md)

  [This release introduces keyboard shortcut indicators for buttons, ensures consistent blob rendering, shows UDOs in the package info, and includes fixes for big number rendering and history position.](platform/v1-20-0.md)
* [v1.19.1 Oct 13, 2025](platform/v1-19-1.md)

  [This release fixes several bugs in the Tenzir Platform; from the Secret Store API to the way ephemeral node tokens are generated.](platform/v1-19-1.md)
* [v1.19.0 Sep 30, 2025](platform/v1-19-0.md)

  [This release adds a new detail page, as well as many UI fixes and improvements.](platform/v1-19-0.md)
* [v1.18.0 Sep 2, 2025](platform/v1-18-0.md)

  [With this release of the Tenzir Platform, we reorganized the UI to make the most important pages more accessible.](platform/v1-18-0.md)
* [v1.17.4 Aug 28, 2025](platform/v1-17-4.md)

  [This patch release contains no public-facing bug-fixes or features.](platform/v1-17-4.md)
* [v1.17.3 Aug 7, 2025](platform/v1-17-3.md)

  [This bugfix release fixes an issue where the Tenzir Platform would generate download URLs with an incorrect signature.](platform/v1-17-3.md)
* [v1.17.2 Aug 6, 2025](platform/v1-17-2.md)

  [You can now select parts of a pipeline from the history pane without closing it and the bottom bar in charts does not overlap with the contant any more.](platform/v1-17-2.md)
* [v1.17.1 Aug 4, 2025](platform/v1-17-1.md)

  [The app now renders durations of length `0` correctly in the detailed event view.](platform/v1-17-1.md)
* [v1.17.0 Jul 30, 2025](platform/v1-17-0.md)

  [This release fixes the display of example pipelines in packages.](platform/v1-17-0.md)
* [v1.16.1 Jul 18, 2025](platform/v1-16-1.md)

  [This release fixes two issues in the Tenzir UI that were found since the last release.](platform/v1-16-1.md)
* [v1.16.0 Jul 16, 2025](platform/v1-16-0.md)

  [This release adds two mechanism for a better diagnostics experience. Diagnostics are now shown directly in the editor. Additionally, the diagnostics heatmap in the pipeline overview can now be interacted with.](platform/v1-16-0.md)
* [v1.15.0 Jul 9, 2025](platform/v1-15-0.md)

  [This release adds support for reading externally-supplied JWT tokens from a header, instead of manually clicking on the *Log In* button.](platform/v1-15-0.md)
* [v1.14.1 Jul 4, 2025](platform/v1-14-1.md)

  [We resolved an issue where some rows in the pipelines table were being cut off. The table now scrolls properly when there are many entries.](platform/v1-14-1.md)
* [v1.14.0 Jul 1, 2025](platform/v1-14-0.md)

  [This release adds CLI support for adding, removing and updating secrets. It also adds a new three-dot menu on the pipelines page, as well as partial pipeline execution from the history.](platform/v1-14-0.md)
* [v1.13.0 Jun 26, 2025](platform/v1-13-0.md)

  [This release contains improved integration for running the Tenzir Platform inside GCP, a new Schema Search functionality, and an option for showing the total diagnostic count in heatmap cells.](platform/v1-13-0.md)
* [v1.12.0 Jun 18, 2025](platform/v1-12-0.md)

  [Tenzir Platform v1.12 introduces an action bar at the bottom of the Explorer, providing easier access to view settings. Additionally, the widget row on the nodes page has been enhanced with numerous improvements and bug fixes.](platform/v1-12-0.md)
* [v1.11.1 Jun 10, 2025](platform/v1-11-1.md)

  [The all-new pipeline widgets make it easy to see at a glance which the total ingress and egress of all pipelines, and to easily figure out which pipelines had warnings and errors.](platform/v1-11-1.md)
* [v1.10.4 Jun 2, 2025](platform/v1-10-4.md)

  [This release adds a custom icon for ephemeral nodes, making them easier to distinguish from regular ones.](platform/v1-10-4.md)
* [v1.10.3 Jun 1, 2025](platform/v1-10-3.md)

  [As of this release, there is a detailed changelog for the Tenzir Platform on the revamped docs.tenzir.com.](platform/v1-10-3.md)
* [v1.10.2 May 21, 2025](platform/v1-10-2.md)

  [This patch release contains a number of additional bugfixes since Tenzir Platform v1.10.1:](platform/v1-10-2.md)
* [v1.10.1 May 20, 2025](platform/v1-10-1.md)

  [This patch release fixes a number of issues found since the release of Tenzir Platform v1.10:](platform/v1-10-1.md)
* [v1.10.0 May 16, 2025](platform/v1-10-0.md)

  [This release restructures the page layout for better usability and adds the ability to statically define workspaces in on-prem environments.](platform/v1-10-0.md)
* [v1.9.7 Apr 17, 2025](platform/v1-9-7.md)

  [This patch release comes with a number of frontend improvements since Tenzir Platform v1.9.6:](platform/v1-9-7.md)
* [v1.9.6 Apr 14, 2025](platform/v1-9-6.md)

  [This patch release includes the following improvements over Tenzir Platform v1.9.5:](platform/v1-9-6.md)
* [v1.9.5 Apr 11, 2025](platform/v1-9-5.md)

  [This patch release includes the following improvements over Tenzir Platform v1.9.4:](platform/v1-9-5.md)
* [v1.9.4 Apr 3, 2025](platform/v1-9-4.md)

  [This patch release includes the following improvements over Tenzir Platform v1.9.3:](platform/v1-9-4.md)
* [v1.9.3 Apr 2, 2025](platform/v1-9-3.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.9.2:](platform/v1-9-3.md)
* [v1.9.2 Mar 18, 2025](platform/v1-9-2.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.9.1:](platform/v1-9-2.md)
* [v1.9.1 Mar 17, 2025](platform/v1-9-1.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.9.0, all of them geared towards Sovereign Edition users:](platform/v1-9-1.md)
* [v1.9.0 Mar 14, 2025](platform/v1-9-0.md)

  [This release revamps the Explorer to better support large datasets.](platform/v1-9-0.md)
* [v1.8.5 Mar 7, 2025](platform/v1-8-5.md)

  [This release does not contain any user-facing changes, only improvements to the internal CI release workflow.](platform/v1-8-5.md)
* [v1.8.4 Mar 6, 2025](platform/v1-8-4.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.8.3:](platform/v1-8-4.md)
* [v1.8.3 Feb 21, 2025](platform/v1-8-3.md)

  [This patch release includes the following bug fixes over Tenzir Platform v1.8.2:](platform/v1-8-3.md)
* [v1.8.2 Feb 19, 2025](platform/v1-8-2.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.8.1:](platform/v1-8-2.md)
* [v1.8.1 Feb 6, 2025](platform/v1-8-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.8:](platform/v1-8-1.md)
* [v1.8.0 Jan 30, 2025](platform/v1-8-0.md)

  [This release adds support for the new and improved charting operators of Tenzir Node v4.27, and revamps example deployments in the platform repository.](platform/v1-8-0.md)
* [v1.7.2 Jan 20, 2025](platform/v1-7-2.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.7.1:](platform/v1-7-2.md)
* [v1.7.1 Jan 14, 2025](platform/v1-7-1.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.7:](platform/v1-7-1.md)
* [v1.7.0 Jan 8, 2025](platform/v1-7-0.md)

  [This release introduces a new Drag'n'Drop feature to easily work with data from local files, and adds additional configuration knobs for Sovereign Edition users.](platform/v1-7-0.md)
* [v1.6.1 Dec 18, 2024](platform/v1-6-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.6:](platform/v1-6-1.md)
* [v1.6.0 Dec 17, 2024](platform/v1-6-0.md)

  [This release features a new UI for example pipelines and adds support for the new TQL2 mode for nodes.](platform/v1-6-0.md)
* [v1.5.0 Dec 6, 2024](platform/v1-5-0.md)

  [This release brings a major upgrade to Dashboards making them independent of nodes.](platform/v1-5-0.md)
* [v1.4.1 Nov 21, 2024](platform/v1-4-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.4:](platform/v1-4-1.md)
* [v1.4.0 Nov 19, 2024](platform/v1-4-0.md)

  [This release introduces **alerts** for the Tenzir Platform, allowing users to get notified when a node is unexpectedly offline.](platform/v1-4-0.md)
* [v1.3.0 Nov 7, 2024](platform/v1-3-0.md)

  [This release introduces a new **vertical layout** option to make better use of the screen space available for event data and longer pipelines:](platform/v1-3-0.md)
* [v1.2.1 Oct 23, 2024](platform/v1-2-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.2:](platform/v1-2-1.md)
* [v1.2.0 Oct 23, 2024](platform/v1-2-0.md)

  [This release brings improvements to diagnostics in the Explorer, adds the ability to download charts, and includes many stability improvements.](platform/v1-2-0.md)
* [v1.1.2 Oct 15, 2024](platform/v1-1-2.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.1.1:](platform/v1-1-2.md)
* [v1.1.1 Oct 11, 2024](platform/v1-1-1.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.1:](platform/v1-1-1.md)
* [v1.1.0 Oct 4, 2024](platform/v1-1-0.md)

  [This release brings key enhancements, including improved diagnostics, authentication updates, and various bug fixes for a smoother user experience.](platform/v1-1-0.md)
* [v1.0.8 Sep 19, 2024](platform/v1-0-8.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.7:](platform/v1-0-8.md)
* [v1.0.7 Sep 16, 2024](platform/v1-0-7.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.6:](platform/v1-0-7.md)
* [v1.0.6 Sep 12, 2024](platform/v1-0-6.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.5:](platform/v1-0-6.md)
* [v1.0.5 Sep 3, 2024](platform/v1-0-5.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.4:](platform/v1-0-5.md)
* [v1.0.4 Aug 26, 2024](platform/v1-0-4.md)

  [This patch release contains the following changes, bug fixes and improvements over Tenzir Platform v1.0.3:](platform/v1-0-4.md)
* [v1.0.3 Aug 13, 2024](platform/v1-0-3.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.0.2:](platform/v1-0-3.md)
* [v1.0.2 Aug 13, 2024](platform/v1-0-2.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.0.1:](platform/v1-0-2.md)
* [v1.0.1 Aug 8, 2024](platform/v1-0-1.md)

  [This patch release contains the following bug fixes and improvements over Tenzir Platform v1.0.0:](platform/v1-0-1.md)
* [v1.0.0 Aug 6, 2024](platform/v1-0-0.md)

  [Tenzir Platform becomes generally available.](platform/v1-0-0.md)
* [v0.20.2 Aug 1, 2024](platform/v0-20-2.md)

  [This bugfix release contains various small fixes and reliability improvements for the Tenzir Platform:](platform/v0-20-2.md)
* [v0.20.1 Jul 18, 2024](platform/v0-20-1.md)

  [This release brings the following improvements and changes:](platform/v0-20-1.md)
* [v0.20.0 Jul 17, 2024](platform/v0-20-0.md)

  [This release brings the following improvements and changes:](platform/v0-20-0.md)
* [v0.19.1 Jul 16, 2024](platform/v0-19-1.md)
  [* This release fixes the CI not triggering for the Tenzir Platform v0.19 release, which caused the release artifacts not to be created.](platform/v0-19-1.md)
* [v0.19.0 Jul 16, 2024](platform/v0-19-0.md)
  [* This release moves pipeline filters into the pipeline table's header, preparing for further upcoming changes to the table \* This release adds a detailed activity view to the detailed pipeline view that opens when clicking on a pipeline \* Clicking on the diagnostics column in the pipelines t...](platform/v0-19-0.md)
* [v0.18.2 Jul 10, 2024](platform/v0-18-2.md)

  [This bugfix release: \* Improves the fix for the memory leak on the overview page \* Fixes an argument parsing bug in the `tenzir-platform admin delete-auth-rule` CLI command](platform/v0-18-2.md)
* [v0.18.1 Jul 8, 2024](platform/v0-18-1.md)
  [* This release fixes a memory leak in the overview page \* This release updates the docker compose examples by automatically pinning them to the corresponding platform version](platform/v0-18-1.md)
* [v0.18.0 Jul 4, 2024](platform/v0-18-0.md)

  [This release introduces diagnostics on the overview page on app.tenzir.com, making it easier to spot mistakes in pipelines. The overview page becomes more responsive when viewing a node with many running pipelines.](platform/v0-18-0.md)
* [v0.17.2 Jul 2, 2024](platform/v0-17-2.md)

  [This release fixes a bug in the `tenzir-platform auth` subcommand.](platform/v0-17-2.md)
* [v0.17.1 Jul 1, 2024](platform/v0-17-1.md)

  [This patch release fixes a bug where very long-running instances of the tenant-manager issue expired user keys, making it impossible for users to log in successfully.](platform/v0-17-1.md)
* [v0.17.0 Jun 21, 2024](platform/v0-17-0.md)

  [This release introduces the ability to change pipelines on app.tenzir.com more quickly. Users can click on any pipeline on the overview page to open a detailed view, directly edit the definition or options, and use the new action menu to quickly start, pause, stop, duplicate, or delete pipelines.](platform/v0-17-0.md)
* [v0.16.0 Jun 7, 2024](platform/v0-16-0.md)

  [This release introduces the initial public version of the on-premise Tenzir Platform for Sovereign Edition customers.](platform/v0-16-0.md)
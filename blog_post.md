# Doggy source control for your Datadog dashboards: 12/10 would sync again

So, you have your Datadog dashboards set up just the way you want them. NO ONE TOUCH ANYTHING. 

We all know that's not realistic. How do you make adjustments (or let other people make adjustments) to your dashboards while being sure you can always go back to a safe known state? Back up your dashboard definitions to source control. Several Datadog community members have created dashboard management tools to do just that.

A great example is [Doggy](https://github.com/Shopify/doggy), a tool from Shopify that stores versioned dashboard definitions as JSON and lets you manage them with git-like commands.

### Getting started with Doggy

To start using Doggy:
1. Create a Github project to store your dashboard definitions.
2. Install Doggy by running:
```
gem install doggy
```
3. Authenticate by exporting the environment variables `DATADOG_API_KEY` and `DATADOG_APP_KEY`, representing your Datadog API and App keys from your Datadog account.

### Managing a dashboard

Suppose you have a dashboard you love and want to maintain and manage. Start by downloading its definition from Datadog to Doggy by running:
```
doggy pull <ID>
```
where `<ID>` is the dashboard's unique identifier. If you don't specify an ID, Doggy downloads the definitions for all your dashboards. You can now commit and push those changes within Github.

If you've made changes to your dashboard and you want to sync that with source control, run: 
```
doggy sync
```
If you want to change what's on Datadog to match what's in source control, run:
```
doggy push <ID>
```
Having your dashboards stored and managed as code is powerful. For example, consider a situation described by Zac Clay in [a write-up about Chargify's Doggy modification](https://inside.chargify.io/2018/02/22/keeping-datadog-in-version-control/): You install an integration that comes with default dashboards, but you want to use a different template variable throughout. Editing all the graphs one by one in the GUI is error-prone and a prescription for RSI. Instead, pull the dashboards down with Doggy, do a search-and-replace on the JSON definition file, and push them back to Datadog with the changed variable name.

### Doggy does more

With Doggy commands, you can also:
* Delete dashboards from Datadog.
* Open a copy of a dashboard in the Datadog UI editor so you can WYSIWYG edit it, and save those changes to the Doggy code, _not_ the Datadog live version. From there you can push to Datadog or discard your changes.
* Mute and unmute monitors.

To get started managing your dashboard configurations, check out [Doggy on Github](https://github.com/chargify/doggy). Big thanks to [Vlad Gorodetsky](https://github.com/bai) at Shopify for this useful tool.

If you have a tool, integration, or client library you've created that uses Datadog API or DogStatsD to improve how you get things done, consider sharing it with the world. Email us at [code@datadoghq.com](mailto:code@datadoghq.com) to tell us about it.

# Contributing Guide

## Before you start

Please, make sure you have read the [readme](README.md).

Also we are f#@*ing happy that you've come here, this is awesome. So, don't hesitate to talk to us.

## Installing

The project contains two sub projects, the front and back end. As always, the front end takes care of the browser side, the funny and beautifull stuff and the back end handles the dark and obscure side.
You find the front end portion in `packages/web` and the back end inside `packages/api`. 

### Web
Make sure you have [yarn](https://classic.yarnpkg.com/en/) installed. In your terminal type:
```bash
$ cd packages/web/
$ yarn
```

## API
Still borning...

## The basics of contributing

A lot of discussions about anything take place in the [issues](https://github.com/lucassouzamatos/dailyr/issues) section. 
We try to keep internal discussions and ideas inside the issues too, but we also try hard to follow milestones and keep an up to date state about current development status. 

### The Git basics

**1. _Fork_ this repository**

There's a button for that in GitHub interface.

**2. Clone your fork of the repository**

```console
$ git clone http://github.com/<YOUR-GITHUB-USERNAME>/dailyr.git
```

**3. Create a feature branch**

```console
$ git checkout -b <YOUR-GITHUB-USERNAME>-new-stuff
```

**4. Do what you do best**

Now it's your time to shine and write meaningful code to raise the bar of the project!

**5. Commit your changes**

```console
$ git commit -am 'My pretty cool contribution'
```

**6. Push to the branch to your fork**

```consle
$ git push origin <YOUR-GITHUB-USERNAME>-new-stuff
```

**7. Create a new _Pull Request_**

From your fork at GitHub usually there is a button to open pull requests.

### Credits
This contributing guide template was adapted from the awesome [serenata-de-amor](https://github.com/okfn-brasil/serenata-de-amor).

localstack-extension-pycharm-debug
==================================

Launch LocalStack and connect it to a PyCharm Debug server for remote debugging LocalStack.

To make use of this extension, you need PyCharm Professional as well as LocalStack Pro.

## Getting started

Steps explained in this guide:

* Install the extension
* Create, in your PyCharm LocalStack project, a Python Debug Server run configuration
* Start LocalStack
* Start debugging

### Installing

Install directly from this repository

```console
localstack extensions install "git+https://github.com/thrau/localstack-extension-pycharm-debug/#egg=localstack-extension-pycharm-debug"
```

### Python Debug Server

#### Create configuration

Create a new [Python Debug Server](https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html) run configuration.

Steps 1. and 2. of the instructions given by PyCharm are handled by this plugin.
The default port LocalStack will connect to is `12345`, so we use that here.
If you want to use a different port, you need to start LocalStack with `PYDEVD_PYCHARM_PORT=<port>`.

![Screenshot at 2023-08-27 17-54-56](https://github.com/thrau/localstack-extension-pycharm-debug/assets/3996682/19ebb30c-3fa5-45f9-971f-91fe75b55df4)

#### Basic path mapping

Before running the server, you should have at least a basic path mapping set up.
In this example we set up
* LocalStack source
* virtual env dependencies

Here's a concrete example:
 
![Screenshot at 2023-08-27 18-01-54](https://github.com/thrau/localstack-extension-pycharm-debug/assets/3996682/9fb718ef-fa90-46ae-a003-6b361f8849a0)

**LocalStack source:**
Say the localstack repository lives in `/home/thomas/workspace/localstack/localstack`, and you have that
attached as project to your IDE,
then you need to map the local source folder to the remote source folder.
In the LocalStack Pro container, localstack is installed as dependency, and therefore lives in the virtual
environment in the container in
`/opt/code/localstack/.venv/lib/python3.10/site-packages/localstack`.

The mapping should be: `/home/thomas/workspace/localstack/localstack/localstack -> /opt/code/localstack/.venv/lib/python3.10/site-packages/localstack`

**Virtual env dependencies:**
For all other sources, we assume they live in your local virtualenv, so we map them to the venv in the container.

The mapping should be `/home/thomas/workspace/localstack/localstack/.venv/lib -> /opt/code/localstack/.venv/lib/`.


#### Start the debug server

Now you can start the debug server and you should see something like:

![Screenshot at 2023-08-27 18-14-31](https://github.com/thrau/localstack-extension-pycharm-debug/assets/3996682/02b606ee-c92e-49c5-a964-52c7de3705d2)

### Start LocalStack

Now start LocalStack, you should see something like:

```
2023-08-27T15:57:06.347  INFO --- [  MainThread] l.extension                : pydevd_pycharm.settrace('172.17.0.1', 12345)
```

If you see a `ConnectionRefusedError: [Errno 111] Connection refused` error, make sure you started the debug
server in PyCharm correctly.

As stated above, if you want to customize the port, run:

```console
localstack start -e PYDEVD_PYCHARM_PORT=23456
```

### Start debugging

The first time localstack connects the debugger will halt execution and show something like:

![Screenshot at 2023-08-27 17-59-43](https://github.com/thrau/localstack-extension-pycharm-debug/assets/3996682/d369ce21-da94-4b13-9222-ddf59a62f1e1)

We can ignore this for now, and simply resume the program by pressing F9.

Now you can set breakpoints in your IDE which will be translated into breakpoints into the running container.
Here's an example debugging the SQS ListQueues operation:

![Screenshot at 2023-08-27 18-06-16](https://github.com/thrau/localstack-extension-pycharm-debug/assets/3996682/9164f613-7add-422f-9347-6da236425714)

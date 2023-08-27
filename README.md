localstack-extension-pycharm-debug
==================================

Launch LocalStack and connect it to a PyCharm Debug server for remote debugging LocalStack.

## Getting started

* Install the extension
* Create, in your PyCharm LocalStack project, a Python Debug Server run configuration
* Start LocalStack
* Start debugging

### Installing

Install from this repository
```console
localstack extensions install file://./dist/localstack_extension_pycharm_debug-0.1.0.dev0-py3-none-any.whl
```

### Python Debug Server

#### Create configuration

Create a new [Python Debug Server](https://www.jetbrains.com/help/pycharm/remote-debugging-with-product.html)
run configuration.
Steps 1. and 2. of the instructions given by PyCharm are handled by this plugin.
The default port LocalStack will connect to is `12345`, so we use that here.
If you want to use a different port, you need to start LocalStack with `PYDEVD_PYCHARM_PORT=<port>`.

#### Basic path mapping

Before running the server, you should have at least a basic path mapping set up.
In this example we set up
* LocalStack source
* virtual env dependencies
 
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


We can ignore this for now, and simply resume the program by pressing F9.

Now you can set breakpoints in your IDE which will be translated into breakpoints into the running container.
Here's an example debugging the SQS ListQueues operation:


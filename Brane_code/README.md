As brane for some reason did not package the code successfully, it was not possible to test the package either, so here is some of the process and experience of packaging, and what the final simple code should look like. The overall code for this topic is written in the root directory, along with the test functions for the overall code.

[https://wiki.enablingpersonalizedinterventions.nl/user-guide/](https://wiki.enablingpersonalizedinterventions.nl/user-guide/)

it describes how to work with Brane for all three of the framework's target roles (system engineers, software engineers and scientists).


[https://wiki.enablingpersonalizedinterventions.nl/admins/](https://wiki.enablingpersonalizedinterventions.nl/admins/)

set the Brane framework up


[https://wiki.enablingpersonalizedinterventions.nl/specification/](https://wiki.enablingpersonalizedinterventions.nl/specification/)

further the understanding of users who want to know exactly what they are working with.


[https://github.com/epi-project/brane](https://github.com/epi-project/brane)

the code repository of brane.

# Three steps installing the framework

* Obtain the relevant binaries (either **by downloading them from the repository** or by compiling them yourself)

* Define initial infrastructures

* Create the images, either **for local use** or **for deployment on a Kubernetes cluster** and run the instance

# Install the Docker

[https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/) -> [https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

* Install using the repository
* Install Docker Engine
## Manage Docker as a non-root user

Manage Docker as a non-root user = https://docs.docker.com/engine/install/linux-postinstall/ -> https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user
# Install the BuildKit plugin for Docker

[https://github.com/docker/buildx](https://github.com/docker/buildx)

 `sudo apt install make`
 # Install Docker compose

# Downloading binaries


Three types of binaries:

* The Command-Line Interface (CLI), which is the `brane` executable. This will only be executed on your local machine.
* The Brane Instance binaries (of which there are multiple), which represent the server part of Brane. These will likely be deployed on a remote server.

* The Branelet executable, which lives inside of the package containers. This will be executed on a Brane instance (i.e., a remote server). ( The branelet executable will automatically be downloaded by the CLI if needed, and so you don't have to download it yourself. )

Download brane: git clone https://github.com/epi-project/brane && cd brane
set the brane to the PATH: export PATH=$PATH:/home/ws/brane/target/release
# Deployment

Two types:

* Deploy the framework on a single Docker engine. We refer to this as  *local deployment* , and it means that **the control plane of the framework runs on a single node**.
* Deploy the framework on multiple nodes with Docker engines. We refer to this as a *distributed deployment* or a  *kubernetes deployment* , and it means that **the control plane of the framework runs on multiple nodes**.

Note that this different only applies to the Brane control plane, **not its jobs**. Regardless of how you deploy it, you are still able to run jobs remotely on different machines.
./make.sh start-instance --precompiled  run the instance, if the binaries are missing, start-instance will automatically attempt to download them (similar to compilation).
## Building the package

the Brane CLI also has a name named 'brane'

```python
brane build ./container.yml
```

Brane will automatically try to deduce the kind of the package based on the name of the file you specify it. `container.yml` will default to an `ecu` package
# Testing your package

```python
brane test hello_world
```

# Publishing your package

( be available in brane instance )

* login `brane login http://127.0.0.1 --username <user>`
* push `brane push hello_world 1.0.0`

# Running your package

connect to the remote instance using the REPL (Read, Eval, Print-Loop) of the Brane CLI tool. ( This loop will take BraneScript statements line-by-line, and run them on the remote instance. Effectively, this will be like "interactively" running a workflow on the remote instance. )

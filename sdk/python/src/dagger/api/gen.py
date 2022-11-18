# Code generated by dagger. DO NOT EDIT.

from typing import NewType

from dagger.api.base import Arg, Root, Type

CacheID = NewType("CacheID", str)
"""A global cache volume identifier"""


ContainerID = NewType("ContainerID", str)
"""A unique container identifier. Null designates an empty container (scratch)."""


DirectoryID = NewType("DirectoryID", str)
"""A content-addressed directory identifier"""


FileID = NewType("FileID", str)

Platform = NewType("Platform", str)

SecretID = NewType("SecretID", str)
"""A unique identifier for a secret"""


class CacheVolume(Type):
    """A directory whose contents persist across runs"""

    async def id(self) -> CacheID:
        """Note
        ----
        This is lazyly evaluated, no operation is actually run.

        Returns
        -------
        CacheID
            A global cache volume identifier
        """
        _args: list[Arg] = []
        _ctx = self._select("id", _args)
        return await _ctx.execute(CacheID)


class Container(Type):
    """An OCI-compatible container, also known as a docker container"""

    def build(self, context: "Directory", dockerfile: str | None = None) -> "Container":
        """Initialize this container from a Dockerfile build"""
        _args = [
            Arg("context", context),
            Arg("dockerfile", dockerfile, None),
        ]
        _ctx = self._select("build", _args)
        return Container(_ctx)

    async def default_args(self) -> list[str] | None:
        """Default arguments for future commands

        Returns
        -------
        list[str] | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("defaultArgs", _args)
        return await _ctx.execute(list[str] | None)

    def directory(self, path: str) -> "Directory":
        """Retrieve a directory at the given path. Mounts are included."""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    async def entrypoint(self) -> list[str] | None:
        """Entrypoint to be prepended to the arguments of all commands

        Returns
        -------
        list[str] | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("entrypoint", _args)
        return await _ctx.execute(list[str] | None)

    async def env_variable(self, name: str) -> str | None:
        """The value of the specified environment variable

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("envVariable", _args)
        return await _ctx.execute(str | None)

    def env_variables(self) -> "EnvVariable":
        """A list of environment variables passed to commands"""
        _args: list[Arg] = []
        _ctx = self._select("envVariables", _args)
        return EnvVariable(_ctx)

    def exec(
        self,
        args: list[str] | None = None,
        stdin: str | None = None,
        redirect_stdout: str | None = None,
        redirect_stderr: str | None = None,
        experimental_privileged_nesting: bool | None = None,
    ) -> "Container":
        """This container after executing the specified command inside it

        Parameters
        ----------
        args:
            Command to run instead of the container's default command
        stdin:
            Content to write to the command's standard input before closing
        redirect_stdout:
            Redirect the command's standard output to a file in the container
        redirect_stderr:
            Redirect the command's standard error to a file in the container
        experimental_privileged_nesting:
            Provide dagger access to the executed command
            Do not use this option unless you trust the command being executed
            The command being executed WILL BE GRANTED FULL ACCESS TO YOUR
            HOST FILESYSTEM
        """
        _args = [
            Arg("args", args, None),
            Arg("stdin", stdin, None),
            Arg("redirectStdout", redirect_stdout, None),
            Arg("redirectStderr", redirect_stderr, None),
            Arg("experimentalPrivilegedNesting", experimental_privileged_nesting, None),
        ]
        _ctx = self._select("exec", _args)
        return Container(_ctx)

    async def exit_code(self) -> int | None:
        """Exit code of the last executed command. Zero means success.

        Null if no command has been executed.

        Returns
        -------
        int | None
            The `Int` scalar type represents non-fractional signed whole
            numeric values. Int can represent values between -(2^31) and 2^31
            - 1.
        """
        _args: list[Arg] = []
        _ctx = self._select("exitCode", _args)
        return await _ctx.execute(int | None)

    async def export(
        self, path: str, platform_variants: "list[Container] | None" = None
    ) -> bool:
        """Write the container as an OCI tarball to the destination file path on
        the host

        Returns
        -------
        bool
            The `Boolean` scalar type represents `true` or `false`.
        """
        _args = [
            Arg("path", path),
            Arg("platformVariants", platform_variants, None),
        ]
        _ctx = self._select("export", _args)
        return await _ctx.execute(bool)

    def file(self, path: str) -> "File":
        """Retrieve a file at the given path. Mounts are included."""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("file", _args)
        return File(_ctx)

    def from_(self, address: str) -> "Container":
        """Initialize this container from the base image published at the given
        address
        """
        _args = [
            Arg("address", address),
        ]
        _ctx = self._select("from", _args)
        return Container(_ctx)

    def fs(self) -> "Directory":
        """This container's root filesystem. Mounts are not included.

        .. deprecated::
            Replaced by :py:meth:`rootfs`.
        """
        _args: list[Arg] = []
        _ctx = self._select("fs", _args)
        return Directory(_ctx)

    async def id(self) -> ContainerID:
        """A unique identifier for this container

        Note
        ----
        This is lazyly evaluated, no operation is actually run.

        Returns
        -------
        ContainerID
            A unique container identifier. Null designates an empty container
            (scratch).
        """
        _args: list[Arg] = []
        _ctx = self._select("id", _args)
        return await _ctx.execute(ContainerID)

    async def mounts(self) -> list[str]:
        """List of paths where a directory is mounted

        Returns
        -------
        list[str]
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("mounts", _args)
        return await _ctx.execute(list[str])

    async def platform(self) -> Platform:
        """The platform this container executes and publishes as"""
        _args: list[Arg] = []
        _ctx = self._select("platform", _args)
        return await _ctx.execute(Platform)

    async def publish(
        self, address: str, platform_variants: "list[Container] | None" = None
    ) -> str:
        """Publish this container as a new image, returning a fully qualified ref

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args = [
            Arg("address", address),
            Arg("platformVariants", platform_variants, None),
        ]
        _ctx = self._select("publish", _args)
        return await _ctx.execute(str)

    def rootfs(self) -> "Directory":
        """This container's root filesystem. Mounts are not included."""
        _args: list[Arg] = []
        _ctx = self._select("rootfs", _args)
        return Directory(_ctx)

    async def stderr(self) -> str | None:
        """The error stream of the last executed command.

        Null if no command has been executed.

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("stderr", _args)
        return await _ctx.execute(str | None)

    async def stdout(self) -> str | None:
        """The output stream of the last executed command.

        Null if no command has been executed.

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("stdout", _args)
        return await _ctx.execute(str | None)

    async def user(self) -> str | None:
        """The user to be set for all commands

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("user", _args)
        return await _ctx.execute(str | None)

    def with_default_args(self, args: list[str] | None = None) -> "Container":
        """Configures default arguments for future commands"""
        _args = [
            Arg("args", args, None),
        ]
        _ctx = self._select("withDefaultArgs", _args)
        return Container(_ctx)

    def with_entrypoint(self, args: list[str]) -> "Container":
        """This container but with a different command entrypoint"""
        _args = [
            Arg("args", args),
        ]
        _ctx = self._select("withEntrypoint", _args)
        return Container(_ctx)

    def with_env_variable(self, name: str, value: str) -> "Container":
        """This container plus the given environment variable"""
        _args = [
            Arg("name", name),
            Arg("value", value),
        ]
        _ctx = self._select("withEnvVariable", _args)
        return Container(_ctx)

    def with_fs(self, id: "DirectoryID") -> "Container":
        """Initialize this container from this DirectoryID

        .. deprecated::
            Replaced by :py:meth:`with_rootfs`.
        """
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("withFS", _args)
        return Container(_ctx)

    def with_mounted_cache(
        self, path: str, cache: "CacheVolume", source: "Directory | None" = None
    ) -> "Container":
        """This container plus a cache volume mounted at the given path"""
        _args = [
            Arg("path", path),
            Arg("cache", cache),
            Arg("source", source, None),
        ]
        _ctx = self._select("withMountedCache", _args)
        return Container(_ctx)

    def with_mounted_directory(self, path: str, source: "Directory") -> "Container":
        """This container plus a directory mounted at the given path"""
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withMountedDirectory", _args)
        return Container(_ctx)

    def with_mounted_file(self, path: str, source: "File") -> "Container":
        """This container plus a file mounted at the given path"""
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withMountedFile", _args)
        return Container(_ctx)

    def with_mounted_secret(self, path: str, source: "Secret") -> "Container":
        """This container plus a secret mounted into a file at the given path"""
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withMountedSecret", _args)
        return Container(_ctx)

    def with_mounted_temp(self, path: str) -> "Container":
        """This container plus a temporary directory mounted at the given path"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withMountedTemp", _args)
        return Container(_ctx)

    def with_rootfs(self, id: "DirectoryID") -> "Container":
        """Initialize this container from this DirectoryID"""
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("withRootfs", _args)
        return Container(_ctx)

    def with_secret_variable(self, name: str, secret: "Secret") -> "Container":
        """This container plus an env variable containing the given secret"""
        _args = [
            Arg("name", name),
            Arg("secret", secret),
        ]
        _ctx = self._select("withSecretVariable", _args)
        return Container(_ctx)

    def with_user(self, name: str) -> "Container":
        """This container but with a different command user"""
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("withUser", _args)
        return Container(_ctx)

    def with_workdir(self, path: str) -> "Container":
        """This container but with a different working directory"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withWorkdir", _args)
        return Container(_ctx)

    def without_env_variable(self, name: str) -> "Container":
        """This container minus the given environment variable"""
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("withoutEnvVariable", _args)
        return Container(_ctx)

    def without_mount(self, path: str) -> "Container":
        """This container after unmounting everything at the given path."""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withoutMount", _args)
        return Container(_ctx)

    async def workdir(self) -> str | None:
        """The working directory for all commands

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("workdir", _args)
        return await _ctx.execute(str | None)


class Directory(Type):
    """A directory"""

    def diff(self, other: "Directory") -> "Directory":
        """The difference between this directory and an another directory"""
        _args = [
            Arg("other", other),
        ]
        _ctx = self._select("diff", _args)
        return Directory(_ctx)

    def directory(self, path: str) -> "Directory":
        """Retrieve a directory at the given path"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    async def entries(self, path: str | None = None) -> list[str]:
        """Return a list of files and directories at the given path

        Returns
        -------
        list[str]
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args = [
            Arg("path", path, None),
        ]
        _ctx = self._select("entries", _args)
        return await _ctx.execute(list[str])

    async def export(self, path: str) -> bool:
        """Write the contents of the directory to a path on the host

        Returns
        -------
        bool
            The `Boolean` scalar type represents `true` or `false`.
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("export", _args)
        return await _ctx.execute(bool)

    def file(self, path: str) -> "File":
        """Retrieve a file at the given path"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("file", _args)
        return File(_ctx)

    async def id(self) -> DirectoryID:
        """The content-addressed identifier of the directory

        Note
        ----
        This is lazyly evaluated, no operation is actually run.

        Returns
        -------
        DirectoryID
            A content-addressed directory identifier
        """
        _args: list[Arg] = []
        _ctx = self._select("id", _args)
        return await _ctx.execute(DirectoryID)

    def load_project(self, config_path: str) -> "Project":
        """load a project's metadata"""
        _args = [
            Arg("configPath", config_path),
        ]
        _ctx = self._select("loadProject", _args)
        return Project(_ctx)

    def with_directory(
        self,
        path: str,
        directory: "Directory",
        exclude: list[str] | None = None,
        include: list[str] | None = None,
    ) -> "Directory":
        """This directory plus a directory written at the given path"""
        _args = [
            Arg("path", path),
            Arg("directory", directory),
            Arg("exclude", exclude, None),
            Arg("include", include, None),
        ]
        _ctx = self._select("withDirectory", _args)
        return Directory(_ctx)

    def with_file(self, path: str, source: "File") -> "Directory":
        """This directory plus the contents of the given file copied to the given
        path
        """
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withFile", _args)
        return Directory(_ctx)

    def with_new_directory(self, path: str) -> "Directory":
        """This directory plus a new directory created at the given path"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withNewDirectory", _args)
        return Directory(_ctx)

    def with_new_file(self, path: str, contents: str) -> "Directory":
        """This directory plus a new file written at the given path"""
        _args = [
            Arg("path", path),
            Arg("contents", contents),
        ]
        _ctx = self._select("withNewFile", _args)
        return Directory(_ctx)

    def without_directory(self, path: str) -> "Directory":
        """This directory with the directory at the given path removed"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withoutDirectory", _args)
        return Directory(_ctx)

    def without_file(self, path: str) -> "Directory":
        """This directory with the file at the given path removed"""
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withoutFile", _args)
        return Directory(_ctx)


class EnvVariable(Type):
    """EnvVariable is a simple key value object that represents an
    environment variable."""

    async def name(self) -> str:
        """name is the environment variable name.

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("name", _args)
        return await _ctx.execute(str)

    async def value(self) -> str:
        """value is the environment variable value

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("value", _args)
        return await _ctx.execute(str)


class File(Type):
    """A file"""

    async def contents(self) -> str:
        """The contents of the file

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("contents", _args)
        return await _ctx.execute(str)

    async def export(self, path: str) -> bool:
        """Write the file to a file path on the host

        Returns
        -------
        bool
            The `Boolean` scalar type represents `true` or `false`.
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("export", _args)
        return await _ctx.execute(bool)

    async def id(self) -> FileID:
        """The content-addressed identifier of the file

        Note
        ----
        This is lazyly evaluated, no operation is actually run.
        """
        _args: list[Arg] = []
        _ctx = self._select("id", _args)
        return await _ctx.execute(FileID)

    def secret(self) -> "Secret":
        _args: list[Arg] = []
        _ctx = self._select("secret", _args)
        return Secret(_ctx)

    async def size(self) -> int:
        """The size of the file, in bytes

        Returns
        -------
        int
            The `Int` scalar type represents non-fractional signed whole
            numeric values. Int can represent values between -(2^31) and 2^31
            - 1.
        """
        _args: list[Arg] = []
        _ctx = self._select("size", _args)
        return await _ctx.execute(int)


class GitRef(Type):
    """A git ref (tag or branch)"""

    async def digest(self) -> str:
        """The digest of the current value of this ref

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("digest", _args)
        return await _ctx.execute(str)

    def tree(self) -> "Directory":
        """The filesystem tree at this ref"""
        _args: list[Arg] = []
        _ctx = self._select("tree", _args)
        return Directory(_ctx)


class GitRepository(Type):
    """A git repository"""

    def branch(self, name: str) -> "GitRef":
        """Details on one branch"""
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("branch", _args)
        return GitRef(_ctx)

    async def branches(self) -> list[str]:
        """List of branches on the repository

        Returns
        -------
        list[str]
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("branches", _args)
        return await _ctx.execute(list[str])

    def commit(self, id: str) -> "GitRef":
        """Details on one commit"""
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("commit", _args)
        return GitRef(_ctx)

    def tag(self, name: str) -> "GitRef":
        """Details on one tag"""
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("tag", _args)
        return GitRef(_ctx)

    async def tags(self) -> list[str]:
        """List of tags on the repository

        Returns
        -------
        list[str]
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("tags", _args)
        return await _ctx.execute(list[str])


class Host(Type):
    """Information about the host execution environment"""

    def directory(
        self,
        path: str,
        exclude: list[str] | None = None,
        include: list[str] | None = None,
    ) -> "Directory":
        """Access a directory on the host"""
        _args = [
            Arg("path", path),
            Arg("exclude", exclude, None),
            Arg("include", include, None),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    def env_variable(self, name: str) -> "HostVariable":
        """Lookup the value of an environment variable. Null if the variable is
        not available.
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("envVariable", _args)
        return HostVariable(_ctx)

    def workdir(
        self, exclude: list[str] | None = None, include: list[str] | None = None
    ) -> "Directory":
        """The current working directory on the host

        .. deprecated::
            Use :py:meth:`directory` with path set to '.' instead.
        """
        _args = [
            Arg("exclude", exclude, None),
            Arg("include", include, None),
        ]
        _ctx = self._select("workdir", _args)
        return Directory(_ctx)


class HostVariable(Type):
    """An environment variable on the host environment"""

    def secret(self) -> "Secret":
        """A secret referencing the value of this variable"""
        _args: list[Arg] = []
        _ctx = self._select("secret", _args)
        return Secret(_ctx)

    async def value(self) -> str:
        """The value of this variable

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("value", _args)
        return await _ctx.execute(str)


class Project(Type):
    """A set of scripts and/or extensions"""

    def extensions(self) -> "Project":
        """extensions in this project"""
        _args: list[Arg] = []
        _ctx = self._select("extensions", _args)
        return Project(_ctx)

    def generated_code(self) -> "Directory":
        """Code files generated by the SDKs in the project"""
        _args: list[Arg] = []
        _ctx = self._select("generatedCode", _args)
        return Directory(_ctx)

    async def install(self) -> bool:
        """install the project's schema

        Returns
        -------
        bool
            The `Boolean` scalar type represents `true` or `false`.
        """
        _args: list[Arg] = []
        _ctx = self._select("install", _args)
        return await _ctx.execute(bool)

    async def name(self) -> str:
        """name of the project

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("name", _args)
        return await _ctx.execute(str)

    async def schema(self) -> str | None:
        """schema provided by the project

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("schema", _args)
        return await _ctx.execute(str | None)

    async def sdk(self) -> str | None:
        """sdk used to generate code for and/or execute this project

        Returns
        -------
        str | None
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("sdk", _args)
        return await _ctx.execute(str | None)


class Client(Root):
    def cache_volume(self, key: str) -> "CacheVolume":
        """Construct a cache volume for a given cache key"""
        _args = [
            Arg("key", key),
        ]
        _ctx = self._select("cacheVolume", _args)
        return CacheVolume(_ctx)

    def container(
        self, id: "ContainerID | None" = None, platform: "Platform | None" = None
    ) -> "Container":
        """Load a container from ID.

        Null ID returns an empty container (scratch).

        Optional platform argument initializes new containers to execute and
        publish as that platform. Platform defaults to that of the builder's
        host.
        """
        _args = [
            Arg("id", id, None),
            Arg("platform", platform, None),
        ]
        _ctx = self._select("container", _args)
        return Container(_ctx)

    async def default_platform(self) -> Platform:
        """The default platform of the builder."""
        _args: list[Arg] = []
        _ctx = self._select("defaultPlatform", _args)
        return await _ctx.execute(Platform)

    def directory(self, id: "DirectoryID | None" = None) -> "Directory":
        """Load a directory by ID. No argument produces an empty directory."""
        _args = [
            Arg("id", id, None),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    def file(self, id: "FileID") -> "File":
        """Load a file by ID"""
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("file", _args)
        return File(_ctx)

    def git(self, url: str, keep_git_dir: bool | None = None) -> "GitRepository":
        """Query a git repository"""
        _args = [
            Arg("url", url),
            Arg("keepGitDir", keep_git_dir, None),
        ]
        _ctx = self._select("git", _args)
        return GitRepository(_ctx)

    def host(self) -> "Host":
        """Query the host environment"""
        _args: list[Arg] = []
        _ctx = self._select("host", _args)
        return Host(_ctx)

    def http(self, url: str) -> "File":
        """An http remote"""
        _args = [
            Arg("url", url),
        ]
        _ctx = self._select("http", _args)
        return File(_ctx)

    def project(self, name: str) -> "Project":
        """Look up a project by name"""
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("project", _args)
        return Project(_ctx)

    def secret(self, id: "SecretID") -> "Secret":
        """Load a secret from its ID"""
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("secret", _args)
        return Secret(_ctx)


class Secret(Type):
    """A reference to a secret value, which can be handled more safely
    than the value itself"""

    async def id(self) -> SecretID:
        """The identifier for this secret

        Note
        ----
        This is lazyly evaluated, no operation is actually run.

        Returns
        -------
        SecretID
            A unique identifier for a secret
        """
        _args: list[Arg] = []
        _ctx = self._select("id", _args)
        return await _ctx.execute(SecretID)

    async def plaintext(self) -> str:
        """The value of this secret

        Returns
        -------
        str
            The `String` scalar type represents textual data, represented as
            UTF-8 character sequences. The String type is most often used by
            GraphQL to represent free-form human-readable text.
        """
        _args: list[Arg] = []
        _ctx = self._select("plaintext", _args)
        return await _ctx.execute(str)

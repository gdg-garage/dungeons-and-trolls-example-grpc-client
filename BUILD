load("@rules_proto_grpc//python:defs.bzl", "python_grpc_compile")

python_grpc_compile(
    name = "dungeonsandtrolls",
    protos = ["@dungeons_and_trolls//proto:dungeonsandtrolls_proto"],
    extra_protoc_args = ["--pyi_out=bazel-out/k8-fastbuild/bin/_rpg_premerge_dungeonsandtrolls"]
)
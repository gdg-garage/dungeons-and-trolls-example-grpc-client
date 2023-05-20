all: proto

deps:
	pip3 install -r requirements.txt

proto: deps
	curl https://raw.githubusercontent.com/gdg-garage/dungeons-and-trolls/main/proto/dungeonsandtrolls.proto -o dungeonsandtrolls.proto
	python -m grpc_tools.protoc -I=. --python_out=. --pyi_out=. --grpc_python_out=. dungeonsandtrolls.proto

bazel-proto:
	bazel build //...
	cp bazel-bin/dungeonsandtrolls/proto/* .
	chmod u+w *

run:
	python3 main.py
Вынес сервис asr в подпакет

## перед релизом:

1. # Обновить .proto (если нужно).

2. python3 -m grpc_tools.protoc -I. \
   --python_out=. \
   --grpc_python_out=. \
   ./my_asr_proto/asr.proto

3. # Проверить, что asr_pb2.py и asr_pb2_grpc.py обновились (diff, git status).

4. # Обновить version= в setup.py (например, 0.2.0).

5. # Собрать локально и протестировать

   python -m build
   или
   python setup.py sdist bdist_wheel
   pip install dist/asr_proto_package-0.2.0-py3-none-any.whl

6. # Закоммитить изменения, поставить git-тег (например, v0.2.0):
   git commit -am "Bump version to 0.2.0"
   git tag v0.2.0
   git push origin main
   git push origin v0.2.0

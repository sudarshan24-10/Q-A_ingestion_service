from repository.abstract.object_storage import ObjectStorageReopository
from minio import Minio
from common.spans.span import Span


class MinioStorageRepository(ObjectStorageReopository):

    def __init__(
        self,
        bucket: str,
        endpoint: str,
        access_key: str,
        secret_key: str,
        secure: bool
    ) -> None:
        self.bucket = bucket
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.secure = secure

        self.client = Minio(
            endpoint=self.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=self.secure
        )

    def fetch_file(self, file_path: str) -> bytes:
        with Span("minio.fetch_file"):
            try:
                with Span("minio.get_object"):
                    obj = self.client.get_object(self.bucket, file_path)

                try:
                    with Span("minio.read_object"):
                        data = obj.read()

                    return data

                finally:
                    with Span("minio.release_connection"):
                        obj.close()
                        obj.release_conn()

            except Exception as e:
                raise e

from .logger import Logger
from datetime import datetime, timedelta

images_to_delete = []


class ECR():
    def __init__(self, log_level) -> None:
        self.log = Logger(log_level)

    # def days_old(self, date) -> int:
    #     current_time = datetime.now().strftime('%Y/%m/%d')
    #     format_current_time = datetime.strptime(current_time, "%Y/%m/%d")
    #     print(format_current_time)
    #     print(date)
    #     delta = format_current_time - date
    #     return delta.days

    def get_images(self, images, age):
        for image in images['imageDetails']:
            current_time = datetime.now()
            create_date = image['imagePushedAt']
            image_digest = image['imageDigest']

            image_format_date = create_date.strftime('%Y/%m/%d')
            current_format_date = current_time.strftime('%Y/%m/%d')

            d1 = datetime.strptime(image_format_date, "%Y/%m/%d")
            d2 = datetime.strptime(current_format_date, "%Y/%m/%d")

            delta = d2 - d1

            if delta.days > age:
                images_to_delete.append(image_digest)
            else:
                self.log.debug(
                    f"{image_digest} will not be delete since is not older than {age} days ago")
        self.log.info(f"Images to delete: {len(images_to_delete)}")
        return images_to_delete

    def delete_images(self, client, repository_name, delete, digest):
        if not delete:
            self.log.info(f"Dry run: deleting {digest}")
            return

        try:
            self.log.info(f"Image {digest} deleted")
            client.batch_delete_image(
                repositoryName=repository_name,
                imageIds=[
                    {
                        'imageDigest': digest,
                    },
                ]
            )
        except Exception as e:
            self.log.warn(f"{e}")

import scratchattach as s3
import os

Secret=os.getenv("Secret")
print(Secret)
Session=s3.login("Boubou78000", Secret)

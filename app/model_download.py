import os
import gdown


def download_model():
    # Buat direktori model jika belum ada
    model_dir = os.path.join(os.path.dirname(__file__), 'model')
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model_path = os.path.join(
        model_dir, 'model_bakteri_inception_resnet_v2.keras')

    # Jika model belum ada, download dari Google Drive
    if not os.path.exists(model_path):
        print("Downloading model from Google Drive...")
        # Ganti URL ini dengan URL Google Drive Anda
        url = 'YOUR_GOOGLE_DRIVE_SHARE_URL'
        gdown.download(url, model_path, quiet=False)
        print("Model downloaded successfully!")

    return model_path

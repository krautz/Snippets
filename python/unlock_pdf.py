import pikepdf


def unlock(filename: str, password: str):
    with pikepdf.open(filename, password=password) as pdf:
        basename, extension = filename.split(".")
        unlocked_filename = f"{basename}_unlocked.{extension}"
        pdf.save(unlocked_filename)

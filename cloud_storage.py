import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.BkRsFjjfG_bsQtfvG3-nUjSqho4pT3WEqXh965QTsqt6TB6qbJpfwwoakdwy8NoyEf_oO6Gx1WpJw6oOfMG2hZTkqaOwXOTMveYLc7ZXRNxEWwjx8a2mtfUxUk8FJ6FMGW2g9Sr4iyvV"
    transferData=TransferData(access_token)

    file_from=input("enter the file path to transfer")
    file_to=input("enter the full path to upload to dropbox ")

    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()

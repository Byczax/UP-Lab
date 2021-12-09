import win32com.client
import os

WIA_COM = "WIA.CommonDialog"

WIA_IMG_FORMAT_PNG = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"

WIA_COMMAND_TAKE_PICTURE = "{AF933CAC-ACAD-11D2-A093-00C04F72DC3C}"


def acquire_image_wia():
    wia = win32com.client.Dispatch(WIA_COM)  # wia is a CommonDialog object
    dev = wia.ShowSelectDevice() # display connected scanners
    
    for i, item in enumerate(dev.Items):
        if i + 1 == dev.Items.Count:
            image = item.Transfer(WIA_IMG_FORMAT_PNG)
            break

    fname = 'wia-test.png'
    if os.path.exists(fname):
        os.remove(fname)
    image.SaveFile(fname)
    if fname.split(".")[-1] == "png":
        os.startfile(fname)

if __name__ == "__main__":
    acquire_image_wia()

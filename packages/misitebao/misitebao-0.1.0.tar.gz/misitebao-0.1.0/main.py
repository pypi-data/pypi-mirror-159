import webbrowser


def main():
    path = "https://misitebao.com"

    try:
        webbrowser.open(path, new=0, autoraise=True)
    except Exception as ex:
        print("An error occurred when opening '%s': %s" % (path, ex))
    else:
        print("Opened '%s' successfully." % path)


if __name__ == '__main__':
    main()

import os
import argparse
import requests # dependency

C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_RED = "\033[91m"
C_END = "\033[0m"

CLASS_ID = 6
MINECRAFT_ID = 432
MODLOADER_ID = 68441

def main():
    parser = argparse.ArgumentParser()

    if "CF_APIKEY" in os.environ:
        parser.add_argument("-k", "--key", type=str, metavar="API_KEY", dest="API_KEY", help="curseforge api key", default=os.environ["CF_APIKEY"])
    else:
        parser.add_argument("API_KEY", type=str, help="curseforge api key")

    parser.add_argument("-i", "--input", type=str, metavar="INPUT_FILE", dest="INPUT_FILE", help="url file to process", required=True)
    parser.add_argument("-v", "--version", type=str, nargs="+", metavar="VERSION", dest="VERSION", help="minecraft version/s", required=True)
    parser.add_argument("-m", "--mod-loader", type=str, metavar="MOD_LOADER", dest="MOD_LOADER", help="minecraft mod loader", required=True)
    parser.add_argument("-o", "--out", type=str, nargs="?", metavar="OUT_DIR", dest="OUT_DIR", help="output directory", default="mods")
    args = parser.parse_args()

    urls = []
    with open(args.INPUT_FILE) as f:
        urls = f.read().splitlines()

    os.makedirs(args.OUT_DIR, exist_ok=True)

    print("CurseForge Minecraft Mod Downloader [Version 1.0.0]")
    print("(c) Adam Charvát, All rights reserved.\n")

    def translateUrl(url):
        url = url.strip()
        slug = url.split("/").pop()
        response = requests.get(
            url=f"https://api.curseforge.com/v1/mods/search?gameId={MINECRAFT_ID}&classId={CLASS_ID}&slug={slug}",
            headers={ "x-api-key": args.API_KEY }
        ).json()
        if len(response["data"]) > 0:
            return response["data"][0]["id"]
        else:
            return None

    # [ URL TRANSLATION STAGE ]

    mods = []
    for url in urls:
        modId = translateUrl(url)
        if modId is not None:
            mods.append({
                "id": modId,
                "url": url
            })
            print(f"Translated url '{C_GREEN}{url}{C_END}' to '{C_BLUE}{modId}{C_END}'.")
        else:
            print(f"Invalid url '{C_RED}{url}{C_END}'.")

    # [ MOD FILE FIND/DOWNLOAD STAGE ]

    errors = []
    success = 0

    for mod in mods:
        url = mod["url"]
        modId = mod["id"]
        latestFile = None
        version = None
        versions = args.VERSION.copy()
        while latestFile == None:
            if len(versions) > 0:
                version = versions.pop(0)
            else:
                print(f"No suitable mod file found for '{C_RED}{url}{C_END}'.")
                errors.append(url)
                break
            response = requests.get(
                url=f"https://api.curseforge.com/v1/mods/{modId}/files?gameVersion={version}",
                headers={ "x-api-key": args.API_KEY }
            ).json()
            if len(response["data"]) > 0:
                for file in response["data"]:
                    modLoaders = []
                    for versionType in file["sortableGameVersions"]:
                        if versionType["gameVersionTypeId"] == MODLOADER_ID:
                            modLoaders.append(versionType["gameVersionName"])
                    if len(modLoaders) > 0:
                        if args.MOD_LOADER in modLoaders:
                            latestFile = file
                            break
                    else:
                        latestFile = response["data"][0]
        if latestFile != None:
            fileId = str(latestFile["id"])
            fileName = latestFile["fileName"]
            fileUrl = latestFile["downloadUrl"]
            if fileUrl == None:
                print(f"The field 'downloadUrl' for '{C_YELLOW}{fileName}{C_END}' is {C_YELLOW}None{C_END}, the program will attempt to create its own download url.")
                #fileUrl = f"{url}/download/{fileId}/file"
                fileUrl = f"https://edge.forgecdn.net/files/{fileId[:4]}/{fileId[4:]}/{fileName}"
            response = requests.get(fileUrl)
            with open(f"{args.OUT_DIR}/{fileName}", "wb") as f:
                f.write(response.content)
            color = C_BLUE if version == args.VERSION[0] else C_YELLOW
            print(f"Downloaded mod file '{C_GREEN}{fileName}{C_END}' for version {color}'{version}'{C_END}.")
            success += 1

    color = C_RED if len(errors) > 0 else C_GREEN
    print(f"\nCompleted with {color}{len(errors)}{C_END} errors, successfully downloaded {C_BLUE}{success}/{len(mods)}{C_END} mods.")

if __name__ == "__main__":
    main()

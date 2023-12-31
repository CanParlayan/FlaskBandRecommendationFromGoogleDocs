import gdown
from colorama import Fore, Style


def download_google_docs(link, output_file):
    print(f"Downloading from: {link}")
    gdown.download(link, output_file, quiet=False, fuzzy=True)
    print(f"Downloaded to: {output_file}")


def get_future_songs_with_plus(file_path):
    Taylan = "T+"
    Baran = "Y+"
    Can = "C+"
    Burak = "B+"

    approvers = {Taylan: Fore.RED, Baran: Fore.BLUE, Can: Fore.GREEN, Burak: Fore.YELLOW}

    future_songs = []
    approvals_count = {approver: 0 for approver in approvers}
    songs_approved_by_everyone = set()
    double_plussed_songs_info = []
    double_plussed_songs = []
    songs_approved_by_everyone_no_parentheses = set()
    approver_approved_songs = {approver: [] for approver in approvers}
    with open(file_path, 'r', encoding='utf-8') as file:

        collecting_future_songs = False

        for line in file:
            line = line.strip()
            if line.startswith("İleride eklenebilecekler"):
                collecting_future_songs = True
                print("Collecting future songs...")
            elif collecting_future_songs:
                print(repr(line))

                approved_by = [approver for approver in approvers if approver in line]
                for approver in approved_by:
                    print(f"{approvers[approver]}{approver} approved this song: {line}{Style.RESET_ALL}")
                    approvals_count[approver] += 1
                    approver_approved_songs[approver].append(line)

                if set(approved_by) == set(approvers):
                    songs_approved_by_everyone.add(line)

                if set(approved_by) == set(approvers) and "(" not in line:
                    songs_approved_by_everyone_no_parentheses.add(line)

                if "++" in line:
                    double_plussed_approver = [approver for approver in approvers if approver in line][0]
                    double_plussed_songs_info.append((line, double_plussed_approver))

    return future_songs, approvals_count, songs_approved_by_everyone, songs_approved_by_everyone_no_parentheses, double_plussed_songs, approver_approved_songs, double_plussed_songs_info


def main():
    doc_link = "https://docs.google.com/document/d/1I5P-SzaiKAOrnPBhnqtoCWDiWrDtSueWodlkjkjegEU/export?format=txt"
    approver_names = {"T+": "Taylan", "Y+": "Baran", "C+": "Can", "B+": "Burak"}

    output_file = "songs.txt"
    download_google_docs(doc_link, output_file)

    approvers = {"T+": Fore.RED, "Y+": Fore.BLUE, "C+": Fore.GREEN, "B+": Fore.YELLOW}

    approved_songs, approvals_count, songs_approved_by_everyone, songs_approved_by_everyone_no_parentheses, double_plussed_songs, approver_approved_songs, double_plussed_songs_info = get_future_songs_with_plus(
        output_file)

    print("\n\nSongs approved by each person:")
    for approver, approved_songs in approver_approved_songs.items():
        print(f"\n{approver_names.get(approver, approver)} tarafından onaylananlar:\n")
        for song in approved_songs:
            print(f"{approvers[approver]}{song}{Style.RESET_ALL}")
    print("\n\n")
    for approver, count in approvals_count.items():
        full_name = approver_names.get(approver, approver)
        print(f"{approvers[approver]}{full_name} {count} şarkıyı onayladı{Style.RESET_ALL}")

    print("\nSongs approved by everyone:\n")
    for song in songs_approved_by_everyone:
        print(f"{Fore.LIGHTMAGENTA_EX}{song}{Style.RESET_ALL}")

    print("\nSongs approved by everyone without excuses:\n")
    for song in songs_approved_by_everyone_no_parentheses:
        print(f"{Fore.MAGENTA}{song}{Style.RESET_ALL}")

    print("\nDouble plussed songs:\n")
    for song, double_plussed_approver in double_plussed_songs_info:
        approver_name = approver_names.get(double_plussed_approver, double_plussed_approver)
        print(
            f"{Fore.CYAN}{approvers[double_plussed_approver]}{approver_name}: {song}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()

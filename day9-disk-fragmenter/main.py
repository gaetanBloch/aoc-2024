from disk_fragmenter import parse_disk_map, compact_disk, compute_checksum


def main():
    with open("input.txt", "r") as file:
        disk_map = file.read().strip()
    print("Raw disk map:")
    blocks = parse_disk_map(disk_map)
    checksum_before = compute_checksum(blocks)
    print(f"Filesystem checksum before compaction: {checksum_before}")
    blocks = compact_disk(blocks)
    checksum_after = compute_checksum(blocks)
    print(f"Filesystem checksum after compaction: {checksum_after}")


if __name__ == "__main__":
    main()

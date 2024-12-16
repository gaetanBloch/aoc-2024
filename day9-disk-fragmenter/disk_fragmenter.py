def parse_disk_map(disk_map):
    """Parses the disk map into a list of blocks."""
    blocks = []
    file_id = 0
    is_file = True  # Start with a file length
    i = 0
    while i < len(disk_map):
        length = int(disk_map[i])
        block_char = str(file_id) if is_file else "."
        blocks.extend([block_char] * length)
        if is_file:
            file_id += 1
        i += 1
        is_file = not is_file
    return blocks


def compact_disk(blocks):
    """Compacts the disk by moving whole files to the leftmost suitable free space."""
    # Identify files with their start and length
    files = {}
    i = 0
    while i < len(blocks):
        if blocks[i] != ".":
            file_id = blocks[i]
            start = i
            length = 0
            while i < len(blocks) and blocks[i] == file_id:
                length += 1
                i += 1
            files[file_id] = length
        else:
            i += 1

    # Sort files by decreasing file ID
    sorted_files = sorted(files.items(), key=lambda x: int(x[0]), reverse=True)

    for file_id, length in sorted_files:
        # Find current position of the file
        current_start = None
        for idx in range(len(blocks)):
            if blocks[idx] == file_id:
                current_start = idx
                break
        if current_start is None:
            continue  # File not found

        # Find the leftmost span of free space that can fit the file
        span_start = None
        span_length = 0
        for idx in range(len(blocks)):
            if blocks[idx] == ".":
                if span_start is None:
                    span_start = idx
                    span_length = 1
                else:
                    span_length += 1
                if span_length == length:
                    break
            else:
                span_start = None
                span_length = 0
        else:
            span_start = None

        if span_start is not None and span_start + length <= current_start:
            # Move the file
            for j in range(length):
                blocks[span_start + j] = file_id
                blocks[current_start + j] = "."
    return blocks


def compute_checksum(blocks):
    """Computes the filesystem checksum."""
    checksum = 0
    for position, block in enumerate(blocks):
        if block != ".":
            checksum += position * int(block)
    return checksum

def validate_raw_puzzle(lines):
    valid_chars = set("#.@+$* ")
    for line in lines:
        for c in line:
            if c not in valid_chars:
                raise ValueError(f"Invalid character: {c}")

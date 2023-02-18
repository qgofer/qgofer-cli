def qgofer_version():
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('version'):
                return line.split('=')[1].strip().strip('"')


def qgofer_name():
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('name'):
                return line.split('=')[1].strip().strip('"')


def qgofer_description():
    with open('./pyproject.toml') as f:
        for line in f:
            if line.startswith('description'):
                return line.split('=')[1].strip().strip('"')


def generate_metadata():
    version = qgofer_version()
    name = qgofer_name()
    description = qgofer_description()
    with (open('./qgofer/metadata.txt', 'w')) as f:
        f.write(f"version={version}\n")
        f.write(f"name={name}\n")
        f.write(f"description={description}\n")


if __name__ == "__main__":
    generate_metadata()

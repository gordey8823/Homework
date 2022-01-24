def make_project(glb_tab, struct, root):
    if glb_tab != -1 and not os.path.exists(root):
        os.mkdir(root)
    os.chdir(root)
    n_stryct = []
    inside_dir = None
    for i, (node_name, line_tab, is_dir) in enumerate(struct):

        if inside_dir:
            if inside_dir[1] < line_tab:
                n_stryct.append((node_name, line_tab, is_dir))
                if i == len(struct) - 1:
                    make_project(inside_dir[1], n_stryct,
                                 os.path.join(root, inside_dir[0]))
            elif inside_dir[1] == line_tab and is_dir:
                make_project(inside_dir[1], n_stryct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab)
                n_stryct = []

            else:

                if not is_dir:
                    n_stryct.append((node_name, line_tab, is_dir))

                make_project(inside_dir[1], n_stryct,
                             os.path.join(root, inside_dir[0]))
                os.chdir(root)
                inside_dir = (node_name, line_tab) if is_dir else None

        elif is_dir:
            inside_dir = (node_name, line_tab)
        else:
            open(node_name, "a").close()


if __name__ == "__main__":
    import os

    with open("config.yaml", "r", encoding="utf-8") as conf_text:
        conf = map(lambda x: (
            x.strip().replace("\t", "  ").replace(":", ""),
            x.rstrip().count(" "),
            x.find(":") > 0
        ), conf_text.readlines())
        print(*conf)

    make_project(-1, list(conf), os.getcwd())

    exit(0)

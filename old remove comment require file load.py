def remove_comments(self, file_path):
        self.open_file()
        with open(file_path, 'r') as file:
            lines = file.readlines()
            new_lines = []
            for line in lines:
                if '#' in line and not (line.strip().startswith(
                        "'") or line.strip().startswith('"')):
                    new_line = line.split('#')[0]
                    new_lines.append(new_line.rstrip() + '\n')
                else:
                    new_lines.append(line)
        self.save_file()
        with open(file_path, 'w') as file:
            file.writelines(new_lines)



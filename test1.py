import sys
import os

matrix = []
final_matrix = []

def main():
    # text_input = "/home/xiongzhengyao/files_4t/mi_files/useful_scripts_all/settings_formate/O3/test.txt"
    if len(sys.argv)!= 2:
        print("Usage: python script.py <text_input> or <folder_path>")
        return
    
    for arg in sys.argv[1:]:
        # print_directory_tree(arg)
        file_name = os.path.basename(arg)
        directory_path = os.path.dirname(arg)
        output_folder = os.path.join(os.path.expanduser(directory_path), 'output')
        # process_input(arg)
        os.makedirs(output_folder, exist_ok=True)
        # print(output_folder)
        # 获取文件名
        
        output_file_path = os.path.join(output_folder, file_name.replace('.txt', '_BOOS.xml'))
        
        get_final_matrix(arg)
        generate_xml(output_file_path)

def print_directory_tree(path):
    if os.path.isfile(path):
        parent_dir = os.path.dirname(path)
        level = len(parent_dir.split(os.sep))
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(path)}")
        current_dir = parent_dir
        while current_dir!= os.sep and current_dir:
            # print(f"{indent}{os.path.basename(current_dir)}/")
            current_dir = os.path.dirname(current_dir)
    else:
        print(f"{path} is not a valid file path.")
def generate_xml(output_file_path):
    
    with open(output_file_path, 'w') as output:
        output.write("<resSettings>\n")  # 开始写入根标签
        for i in range(len(final_matrix)):
            try:
                output.write("        <regSetting>\n")
                output.write(f"          <registerAddr>{final_matrix[i][0]}</registerAddr>\n")
                output.write(f"          <registerData>{final_matrix[i][1]}</registerData>\n")
                output.write("          <regAddrType range=\"[1,4]\">2</regAddrType>\n")
                output.write("          <regDataType range=\"[1,4]\">2</regDataType>\n")
                if len(final_matrix[i][1]) <= 6:
                    output.write("          <operation>WRITE</operation>\n")
                else:
                    output.write("          <operation>WRITE_BURST</operation>\n")
                output.write("          <delayUs>0x0000</delayUs>\n")
                output.write("        </regSetting>\n")
            except ValueError:
                continue
        output.write("      </resSettings>\n")  # 闭合根标签
def get_final_matrix(text_input):

    linenum = 0
    with open(text_input, 'r') as file:
        # print("Text input:", text_input)
        for line in file:
            columns = line.strip().split()
            if len(columns) >= 2:
                columns[0] = f"0x{columns[0]}"
                columns[1] = f"0x{columns[1]}"
                matrix.append(columns)

    for i in range(len(matrix)):
        if i == 0:
            final_matrix.append(matrix[i])
            # linenum = linenum + 1
            continue
        else:
            if (int(matrix[i][0], 16) == int(matrix[i-1][0], 16) + 2 ) and ((len(final_matrix[linenum][1])) <= 210*7-1):
                if (len(final_matrix[linenum]) == 2):
                    if len(final_matrix[linenum]) > 1 :
                        final_matrix[linenum][1] = f"{final_matrix[linenum][1]} {matrix[i][1]}"
                # else:
                #     print(columns[i][1])

            else:
                final_matrix.append(matrix[i])
                linenum = linenum + 1

    # print(final_matrix)
    # 假设 final_matrix 已经是填充好的二维数组
    for index, row in enumerate(final_matrix):
        # 检查当前行是否有足够的列
        if len(row) > 1:
            # 打印第二列的长度
            print(f"Row {index + 1}, second column size: {len(row[1])}")
        else:
            # 如果当前行没有第二列，则打印提示信息
            print(f"Row {index + 1} does not have a second column")

if __name__ == "__main__":
    main()

### 설명용
P_num="003"
file_type="py"
IO_Test_Case=1

File_name=${P_num}.${file_type};

if [ $file_type == "py" ]; then
    for ((i=0; i<${IO_Test_Case}; i++));
    do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
fi

### 터미널 붙여넣기용
P_num="003";file_type="py";IO_Test_Case=1;File_name=${P_num}.${file_type};
if [ $file_type == "py" ]; then for ((i=0; i<${IO_Test_Case}; i++));    do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
fi
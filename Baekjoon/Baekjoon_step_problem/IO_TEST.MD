P_num="test";file_name="1.스택";file_type="py";IO_Test_Case=2;File_name=${file_name}.${file_type};
if [ $file_type == "py" ]; then for ((i=0; i<${IO_Test_Case}; i++));    do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
fi

### 파일 생성 (순차)
P_num="test";
IO_Test_Case=2;
for ((i=0; i<${IO_Test_Case}; i++));
do
    input_file=${P_num}_input${i}.txt;
    output_file=${P_num}_output${i}.txt;
    answer_file=${P_num}_answer${i}.txt;
    touch ${input_file}
    touch ${output_file}
    touch ${answer_file}
done;
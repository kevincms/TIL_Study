P_num="test";file_name="5.덱";file_type="py";IO_Test_Case=2;File_name=${file_name}.${file_type};
if [ $file_type == "py" ]; then for ((i=0; i<${IO_Test_Case}; i++));    do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
fi

P_num="test";file_name="19_5";file_type="cpp";IO_Test_Case=2;File_name=./${file_name}.exe;
if [ $file_type == "py" ]; then File_name=${P_num}.py; for ((i=0; i<${IO_Test_Case}; i++)); do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
elif [ $file_type == "exe" ]; then 
    File_name=./${file_name}.exe;
    for ((i=0; i<${IO_Test_Case}; i++)); do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        ${File_name} < ${input_file} > ${output_file};
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
### 테스트 - 설명용
P_num="003";
file_type="py";
IO_Test_Case=1;

File_name=${P_num}.${file_type};

if [ $file_type == "py" ]; then;
    for ((i=0; i<${IO_Test_Case}; i++));
    do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
fi

### 테스트 - 터미널 붙여넣기용
> - do it
P_num="test";file_type="py";IO_Test_Case=2;File_name=${P_num}.${file_type};
if [ $file_type == "py" ]; then for ((i=0; i<${IO_Test_Case}; i++));    do
        input_file=${P_num}_input${i}.txt;
        output_file=${P_num}_output${i}.txt;
        answer_file=${P_num}_answer${i}.txt;
        python ${File_name} < ${input_file} > ${output_file};
        diff ${output_file} ${answer_file};
    done;
fi

> - 일반
P_num="test";file_name="5.RGB거리";file_type="py";IO_Test_Case=5;File_name=${file_name}.${file_type};
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
IO_Test_Case=5;
for ((i=0; i<${IO_Test_Case}; i++));
do
    input_file=${P_num}_input${i}.txt;
    output_file=${P_num}_output${i}.txt;
    answer_file=${P_num}_answer${i}.txt;
    touch ${input_file}
    touch ${output_file}
    touch ${answer_file}
done;

### 파일 생성 (개별)
P_num="022";
IO_Test_Num=1;
input_file=${P_num}_input${IO_Test_Num}.txt;
output_file=${P_num}_output${IO_Test_Num}.txt;
answer_file=${P_num}_answer${IO_Test_Num}.txt;
touch ${input_file}
touch ${output_file}
touch ${answer_file}
public class J1_print {
    public static void main(String[] args) {
        String[] language={"Python","Java","C","C++","Go","JavaScript","Swift","C#"};
        int count=1;

        System.out.print(count+++". "+language[count-1]+"\n"); // 1. pythonó�� +�� ������ �� �ִ�.

        System.out.println(count+++". "+language[count-1]); // 2. println�� �ڵ������� �� �ٲ��� �ȴ�.

        System.out.printf("%d. %s",count++,language[count-1]); // 3. C�� ���� printf�� ����� �� �ִ�.
    }
    /*
    vscode �ڵ��ϼ�
    - main
    public static void main(String[] args) {
    }
    - sysout
    System.out.println();
    - print (Ŀ����) 
    Ctrl+5hift+P -> User Snippets
    System.out.printf();
        "System.out.printf": {
            "prefix": "print",
            "body": [
                "System.out.printf(\"$1\\n\");"
            ],
            "description": "System.out.printf"
        }
    */
}

public class J3_data_type_variable {
    public static void main(String[] args) {
        int count=1;

        int test_int=1;
        System.out.printf("%d. %d\n",count++,test_int); // 1. 정수

        double test_float=1.1;
        System.out.printf("%d. %f\n",count++,test_float); // 2. 실수

        double test_double=1.1;
        System.out.printf("%d. %f\n",count++,test_double); // 3. 실수 (float보다 범위가 큼)
        
        char test_char='a';
        System.out.printf("%d. %c\n",count++,test_char); // 4. 문자
    
        String test_string="Hello World";
        System.out.printf("%d. %s\n",count++,test_string); // 5. 문자열

        boolean test_bool=true;
        System.out.printf("%d. %b\n",count++,test_bool); // 6. 참과 거짓
    }
}

// Nodejs의 경우 console.log로 출력할 수 있다.
language=["Python","C","Nodejs","C++","Go","JavaScript","Swift","C#"]
count=1

// +로 문자열과 변수를 섞어 출력할 수 있다.
console.log(count+". "+language[count++-1])

// ,로 문자열과 변수를 섞어 출력할 수 있다. (단 +와 달리 자동으로 한칸 공백이 생긴다.)
temp_count=String(count)+"."
console.log(temp_count,language[count++-1])

// `를 이용해 문자열안에 변수를 ${}로 넣을 수 있다. (`=키보드 ~ 위치)
console.log(`${count}. ${language[count++-1]}`,)
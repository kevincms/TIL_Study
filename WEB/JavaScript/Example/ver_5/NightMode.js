function NightdayMode(self){
    if(self.value==='야간 모드 켜기'){
        document.querySelector('body').style.backgroundColor='black';
        document.querySelector('body').style.color='white';
        self.value='야간 모드 끄기'
        var hyperlink = document.querySelectorAll('a')
        for(var i=0; i<hyperlink.length; i++){
            hyperlink[i].style.color='powderblue';
        }
    }
    else if(self.value==='야간 모드 끄기'){
        document.querySelector('body').style.backgroundColor='white';
        document.querySelector('body').style.color='black';
        self.value='야간 모드 켜기'
        var hyperlink = document.querySelectorAll('a')
        for(var i=0; i<hyperlink.length; i++){
            hyperlink[i].style.color='blue';
        }
    }
}
ALT::return

!k:: Send {Down}
+!k:: Send +{Down}
!i:: Send {Up}
+!i:: Send +{Up}
!j:: Send {Left}
+^!j:: Send ^+{Left}
^!j:: Send ^{Left}
+!j:: Send +{Left}
!l:: Send {Right}
+^!l:: Send ^+{Right}
^!l:: Send ^{Right}
+!l:: Send +{Right}

!u:: Send {Home}
+!u:: Send +{Home}
!o:: Send {End}
+!o:: Send +{End}
!h:: Send {Del}
+!h:: Send +{Del}
!y:: Send {Ins}
+!y:: Send +{Ins}
!p:: Send {PgUp}
+!p:: Send +{PgUp}
!`;:: Send {PgDn}
+!`;:: Send +{PgDn}
!n:: Send {BackSpace}

!2:: Send {F2}
!4:: Send !{F4}
^5:: Send ^{F5}
!5:: Send {F5}
+!5:: Send +{F5}
+!ESC:: Send ~

!z:: Send 1
!x:: Send 2
!c:: Send 3
!a:: Send 4
!s:: Send 5
!d:: Send 6
!q:: Send 7
!w:: Send 8
!e:: Send 9
!r:: Send 0

!f:: Send {Del}
!v:: Send {BackSpace}

NSet = 0

#n:: 
  If  (NSet = 1 ) 
  { 
    NSet = 0
  } 
  else 
  {  
    NSet = 1
  }
return

#if NSet = 1
{
	u::4
	i::5
	o::6
	j::1
	k::2
	l::3
	m::0
  w:: Send {Up}
  s:: Send {Down}
  a:: Send {Left}
  d:: Send {Right}
  H:: Send {Del}
  y:: Send {Ins}
  p:: Send {PgUp}
  `;:: Send {PgDn}
  ,:: Send {Home}
  .:: Send {End}
}
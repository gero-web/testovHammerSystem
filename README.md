Сайт доступен по хостингу http://sergeq.pythonanywhere.com/  

Краткое описание API 
доступно в redoc: https://sergeq.pythonanywhere.com/schema/redoc/

1) запрос login --- /auth/login/
	Методот запроса POST возвращаемый параметер otp код
	Пример json
	{
    		"user_phone": "string"
	}
	Пример ответа 
	{
   		 "otp": int
	}
	
2) запрос otp --- auth/otp_validation/
	Методот запроса POST возвращаемый параметеры access и  refresh  для jwt авторизации 
	пример запроса 
	{
  		  "otp": "string"
	}
	в случае проблемы с сессией нужно передать дополнительный параметер user_phone
	Пример запроса 
	{
		  "user_phone": "string",
  		  "otp": "string"
	}

3) profile -- profile/
Методот запроса GET возвращаемый параметер объект Profile, доступен только авторизованым пользователям
	{
   		"name": string,
  		"phone": string,
    		"invate": string,
  		"someone_invite": string,
   		"users": [] or [
			{
				"name": string,
  				"phone": string,
    				"invate": string,
  				"someone_invite": string,
			}
		]
	}
	 
4) profile -- profile/
Методот запроса PUT ,доступен только авторизованым пользователям
	Редактирует профиль пользователя 
	пример запроса 
	{
   	    "someone_invite": "789793"
	}
	пример ответа
     	{
    		"msg": "Update"
	}

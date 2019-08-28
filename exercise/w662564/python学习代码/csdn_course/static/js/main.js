        var show= function(id){
            //清空提示信息
            document.getElementById('register_message').innerText='';
            document.getElementById('login_message').innerText='';

            //如果是注册，则不显示登录，反之亦然
            if (id==='register'){
                document.getElementById(id).hidden = false;
                document.getElementById('login').hidden = true;
            }else{
                document.getElementById(id).hidden = false;
                document.getElementById('register').hidden = true;
            }
        };
        window.onload =function(){
            //账号和密码的正则表达式
            var account_pattern = /[a-zA-Z0-9_]{8,16}/;//字母、数字、下划线，8-16位
            var password_pattern = /[a-zA-Z0-9_]{6,16}/;//字母、数字、下划线、6-16位
            //注册时验证表单数据，return false为组织表达提交
            document.getElementById('register_form').onsubmit = function(){
                //得到表单中的账号
                account = document.getElementById('register_account').value;
                //得到表单中的密码
                password = document.getElementById('register_password').value;
                //得到用于提示的P标签节点
                messageElement = document.getElementById('register_message');
                //验证账号
                if (! account_pattern.test(account)){
                    messageElement.innerText = '账号格式非法';
                    return false;
                };
                //验证密码
                if (! password_pattern.test(password)){
                    messageElement.innerText = '密码格式非法';
                    return false;
                };
                //如果验证都通过，return true,允许表单提交
                return true;

            };
            //注册时验证表单数据，return false为组织表达提交
            document.getElementById('login_form').onsubmit = function(){
                //得到表单中的账号
                account = document.getElementById('login_account').value;
                //得到表单中的密码
                password = document.getElementById('login_password').value;
                //得到用于提示的P标签节点
                messageElement = document.getElementById('login_message');
                //验证账号
                if (! account_pattern.test(account)){
                    messageElement.innerText = '账号格式非法';
                    return false;
                };
                //验证密码
                if (! password_pattern.test(password)){
                    messageElement.innerText = '密码格式非法';
                    return false;
                };
                return true;
            }
        }
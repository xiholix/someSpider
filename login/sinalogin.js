/**
 * Created by xie on 17-2-7.
 */


    function    get_pass(mypass,nonce,servertime,rsakey){

            varRSAKey = newsinaSSOEncoder.RSAKey();

            RSAKey.setPublic(rsakey,"10001");

            password= RSAKey.encrypt([servertime,nonce].join("\t") +"\n"+ mypass)

            return    password

    }

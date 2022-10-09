
//     Ja


function get_token(){
    Java.perform(function() {


        Java.use("com.mcdonalds.androidsdk.core.hydra.e").a.overload().implementation  = function(){
            return false
        }


        var token = Java.use("com.akamai.botman.CYFMonitor").a.overload().call(Java.use("com.akamai.botman.CYFMonitor"))
        send(token.toString())
        return token
    });
}


rpc.exports = {
    getToken: get_token,
};
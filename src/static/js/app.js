document.addEventListener('DOMContentLoaded', function() {
    console.log("페이지가 로드되었습니다!");
    // 여기에 추가적인 JavaScript 로직을 넣을 수 있습니다.
});

(function() {
    console.log("@@");
    // params formatting
    // {
    //   request: "xxxx"
    // }
    // response formatting
    // {
    //   success: true|false,
    //   value: data
    //   message: message
    // }
    ajax = {
        // showError is callback for debugging
        showError : function(title, message){},
        get : function(url, params, callback) {
          var opts = {
            dataType : 'json',
            type : 'GET',
            async : true,
            contentType: "application/json",
            url : url,
            data : JSON.stringify(params),
          };
          this.do_ajax(opts, callback);
        },
        post :function(url, params, callback) {
          var opts = {
            dataType : 'json',
            type : 'POST',
            contentType: "application/json",
            async : true,
            url : url,
            data : JSON.stringify(params),
          };
          this.do_ajax(opts, callback);
        },
        put :function(url, params, callback) {
          var opts = {
            dataType : 'json',
            type : 'PUT',
            contentType: "application/json",
            async : true,
            url : url,
            data : JSON.stringify(params),
          };
          this.do_ajax(opts, callback);
        },
        patch :function(url, params, callback) {
          var opts = {
            dataType : 'json',
            type : 'PATCH',
            contentType: "application/json",
            async : true,
            url : url,
            data : JSON.stringify(params),
          };
          this.do_ajax(opts, callback);
        },
        delete :function(url, params, callback) {
          var opts = {
            dataType : 'json',
            type : 'DELETE',
            contentType: "application/json",
            async : true,
            url : url,
            data : JSON.stringify(params),
          };
          this.do_ajax(opts, callback);
        },
        do_ajax : function(opts, callback) {
          opts.success = function(resp) {
            // console.log(JSON.stringify(resp));
            if (callback && resp.success) {
              // console.log('ajax', resp);
              callback(resp.value);
              if (resp.message) {
                console.log("success::"+resp.message);
              }
            } else if (resp.success == false) {
              var emsg = opts.type+': '+opts.url;
              emsg += '\nMessage: ' + resp.message;
              console.log("fail::"+emsg);
              if (typeof ajax.showError === 'function') {
                console.log("fail@@"+emsg);
                ajax.showError('FAIL', emsg);
              }
            }
          } ,
          opts.error = function(resp) {
            var emsg = opts.type+': '+opts.url;
            emsg += '\nMessage: ' + resp.message;
            console.log("error::"+emsg);
            if (typeof ajax.showError === 'function') {
              ajax.showError('ERROR', emsg);
            }
          }
          $.ajax(opts);
        },
      };
    
})();
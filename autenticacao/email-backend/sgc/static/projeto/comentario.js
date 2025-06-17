$(document).ready(function(){
    $('#comment-btn').click(function(){
        if (!!$('#comment-area').val()){
            $.ajax({
                type : 'GET',
                url : '/projeto/comentar/',
                data : { comentario : $('#comment-area').val(), projeto: $('#projetoId').val()},
                success : function(response) {    
                    
                    if (response.status === 'ok'){
                        var commentsNode = document.getElementById('comment-list');
                        nodeCard = document.createElement('div');
                        nodeCard.className = "card p-3";
                        
                        nodeFlex = document.createElement('div');
                        nodeFlex.className = "d-flex justify-content-between align-items-center";
                        nodeUser = document.createElement('div');
                        nodeUser.className = "user d-flex flex-row align-items-center overflow-auto text-break";

                        nodeUserSpan = document.createElement('span');
                        nodeUserSpanSmallUser = document.createElement('small');
                        nodeUserSpanSmallUser.className = "font-weight-bold text-primary";
                        nodeUserSpanSmallSmall = document.createElement('small');
                        nodeUserSpanSmallSmall.className = "font-weight-bold";

                        nodeCard.appendChild(nodeFlex);
                        nodeFlex.appendChild(nodeUser);
                        nodeUser.appendChild(nodeUserSpan);
                        nodeUserSpan.appendChild(nodeUserSpanSmallUser);
                        nodeUserSpan.appendChild(nodeUserSpanSmallSmall);
                        nodeUserSpanSmallUser.appendChild(document.createTextNode("usuário "));
                        nodeUserSpanSmallSmall.appendChild(document.createTextNode(response.texto))


                        nodeDays = document.createElement('small');
                        nodeDays.appendChild(document.createTextNode("2 days ago"));
                        nodeFlex.appendChild(nodeDays);

                        nodeAction = document.createElement('div');
                        nodeAction.className = "action d-flex justify-content-between mt-2 align-items-center"
                        nodeReply = document.createElement('div');
                        nodeReply.className = "reply px-4";
                        nodeSmallRemover = document.createElement('small');
                        nodeSmallRemover.appendChild(document.createTextNode("Remover "));
                        nodeSpanDots1 = document.createElement('span');
                        nodeSpanDots1.className = "dots"
                        nodeSmallResponder = document.createElement('small');
                        nodeSmallResponder.appendChild(document.createTextNode(" Responder"));


                        nodeCard.appendChild(nodeAction);
                        nodeAction.appendChild(nodeReply);
                        nodeReply.appendChild(nodeSmallRemover);
                        nodeReply.appendChild(nodeSpanDots1);
                        nodeReply.appendChild(nodeSmallResponder);


                        commentsNode.appendChild(nodeCard);
                    }
                    console.log(response);  

                },
                error : function(response){
                    alert(response.error);        
                }
            })
        }else{
            console.log("error");
        }
    });
});
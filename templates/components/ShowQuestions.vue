<template>
  <div id="showquest">

    <header1></header1>
    <div class="container layout layout-margin-top" style="text-align:left">

      <ol class="breadcrumb">
        <li><a href="/questions/">讨论区</a></li>
        <li>实验报告</li>
        <li class="active">
          <a href="javascript:;">
            {{myquestlist.report_title}}
          </a>
        </li>
      </ol>

      <div class="row">
        <div class="col-md-9 layout-body">

          <div class="content question-detail">
            <div class="question-headline">
              <span class="question-title"> {{myquestlist.report_title}}</span>
              <span class="question-figure">{{myquestlist.linknum}} 回复</span><span
              class="question-figure">{{myquestlist.report_browse}} 查看</span>
            </div>
            <div class="question-author">


              <div class="user-avatar ">
                <a class="avatar" href="javascript:;" target="_blank">
                  <img :src="myquestlist.pic">
                </a>

              </div>


              <div class="user-username ">
                <a class="username" href="javascript:;" target="_blank">

                  {{myquestlist.username}}


                </a>
                <!--                <span class="user-level">{{myquestlist.userlevel}}</span>-->
              </div>

              <span> {{myquestlist.create_time}}</span>

<!--              <span><a href="/questions/?area_type=course">课程问答</a></span>-->


<!--              <span class="question-from">来自： <a href="javascript:;">熟悉实验环境 </a></span>-->


<!--              <a href="#sign-modal" data-toggle="modal" data-sign="signin"-->
<!--                 class="btn btn-primary collectBtn disabled">收藏</a>-->
            </div>
            <div class="question-content markdown-body">
              <div v-html="myquestlist.report_content"></div>
              <p></p>


              <div class="labreport-detail-like">

    <span class="btn btn-default btn-weiboshare disabled">
        <i class="fa fa-share-alt"></i>
    </span>
              </div>

            </div>

            <div class="question-answers">
              <p class="ptilte">全部回复</p>
              <hr/>
              <div class="answer-item" v-for="(i,index) in reportcomment" :key="index">
                <div class="answer-head">


                  <div class="user-avatar ">
                    <a class="avatar" href="javascript:;" target="_blank">
                      <img :src="i.img">
                    </a>

                  </div>

                </div>
                <div class="answer-detail">
                    <span class="comment-reply">




    <div class="user-username ">
        <a class="username" href="javascript:;" target="_blank">

                {{i.username}}


        </a>
        <span class="user-level">{{i.userlevel}}</span>
    </div>

                    </span>

                  <div class="answer-content markdown-body">
                    <div>{{i.content}}</div>
                  </div>


                  <div>
                    <span class="create-time">{{i.create_time}}</span>
                    &nbsp;&nbsp;&nbsp;回复:&nbsp;{{i.back_username}}
                    <div :style="{'text-align':'right'}"><img src="../../static/img/下载.png" alt=""
                                                              width="5px" height="20px">
                      <span @click="show(i)">回复</span>
                    </div>
                    <hr/>
                  </div>
                </div>

              </div>

            </div>
            <div class="your-answer words-ctrl">

              <p style="text-align: center;font-weight: 300; font-size: 18px;" v-if="user_id ==null">
                <a href="#sign-modal" data-toggle="modal" data-sign="signin"
                   data-next="/questions/8641">登录</a>后回复帖子

              </p>
              <div style="text-align: center;font-weight: 300; font-size: 18px;" v-else>
                                <textarea name="" id="" cols="88" rows="10" v-model="content"
                                          placeholder="在这里发表你的看法和建议!"
                                          :style="{'outline':'none','border-radius':'25px','background':'#ebfff2'}"></textarea>
                <div :style="{'float':'right','text-align':'right','padding-right':'10px','border-radius':'25px'}">
                  <button
                    :style="{'border-radius':'25px','background':'#ebfff2'}" type="submit"
                    value="评论" width="80px" @click="addreport">发表评论
                  </button>
                </div>
              </div>

            </div>
          </div>

        </div>
        <div class="col-md-3 layout-side">

          <a class="btn side-btn" data-toggle="modal" data-target="#askquestion">我要发帖</a>
          <div class="side-image">
            <a href="/vip" target="_blank">
              <img src="https://static.shiyanlou.com/img/banner-vip.png">
            </a>
          </div>
          <div class="sidebox side-list related-question">
            <div class="sidebox-header">
              <h4 class="sidebox-title">相关帖子</h4>
            </div>
            <div class="sidebox-body side-list-body">
            </div>
          </div>

        </div>
      </div>
    </div>
    <div class="modal fade askquestion-modal" id="coummm" tabindex="-1" role="dialog">
      <div class="modal-dialog" role=document>
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title">回复</h4>
          </div>
          <div class="modal-body words-ctrl">
            <form class="form-horizontal" action="/questions/">
              <input name="_csrf_token" type=hidden
                     value="1483794941##be4fb68b276c5f7cb970936cb25985cd53b943d1">
              <div class="form-group">
                <label class="col-md-2 control-label">描述</label>
                <div class="col-md-10">


                  <div class="tabpanel mkeditor">
                    <ul class="nav nav-tabs" role="tablist">
                      <li role="presentation" class="active">
                        <a href="#mkeditor-editor" role="tab" data-toggle="tab">编辑</a>
                      </li>
                      <li role="presentation">
                        <a class="mkeditor-btn-view" href="#mkeditor-viewer" role="tab"
                           data-toggle="tab">预览</a>
                      </li>
                    </ul>
                    <div class="tab-content">
                      <div class="tab-pane active mkeditor-editor" id="mkeditor-editor"
                           role="tabpanel">

                        <div class="btn-group" role="group">

                          <button type="button" class="btn btn-default mkeditor-btn-bold">
                            <i class="fa fa-bold"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-italic">
                            <i class="fa fa-italic"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-link">
                            <i class="fa fa-link"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-quote">
                            <i class="fa fa-quote-left"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-code">
                            <i class="fa fa-code"></i>
                          </button>
                          <button id="mkeditor-pickfile" type="button"
                                  class="btn btn-default mkeditor-btn-img">
                            <i class="fa fa-image"></i>
                          </button>

                          <button type="button" class="btn btn-default mkeditor-btn-listol">
                            <i class="fa fa-list-ol"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-listul">
                            <i class="fa fa-list-ul"></i>
                          </button>
                        </div>
                        <div class="btn-group pull-right" role="group">
                          <a style="font-size:12px; color:#666; text-decoration:underline;"
                             href="/questions/764" target="_blank">
                            <i class="fa fa-question-circle"></i>Markdown 语法
                          </a>
                        </div>
                        <textarea name="content" class="content" min="0" max="20000"
                                  placeholder="推荐使用 Markdown 语法，至少输入 5 个字"
                                  v-model="content"></textarea>
                        <div class="help-block"></div>
                      </div>
                      <div class="tab-pane mkeditor-viewer markdown-body" id="mkeditor-viewer"
                           role="tabpanel">
                        <div></div>
                      </div>
                    </div>
                  </div>

                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal"
                    @click="backWrite">提交
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
          </div>
          <div class="modal-body">

            <div><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！
            </h4></div>

            <div id="msg-modal"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="flash-message" tabindex="-1" role="dialog">
      <div class="modal-dialog" rolw="document">
      </div>
    </div>
    <div class="modal fade" id="modal-message" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
              class="sr-only">Close</span></button>
            <h4 class="modal-title">注意</h4>
          </div>
          <div class="modal-body">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary confirm" data-dismiss="modal">确定</button>
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade askquestion-modal" id="askquestion" tabindex="-1" role="dialog">
      <div class="modal-dialog" role=document>
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title">发帖</h4>
          </div>
          <div class="modal-body words-ctrl">
            <form class="form-horizontal" action="/questions/">
              <input name="_csrf_token" type=hidden
                     value="1483797676##818560cdc39a2ed99c488cf67125c1f53c60ad03">
              <div class="form-group">
                <label class="col-md-2 control-label">标题</label>
                <div class="col-md-10">
                  <input type="text" name="title" min="5" max="100" class="form-control"
                         placeholder="至少输入5个字" value="">
                  <span class="help-block"></span>
                </div>
              </div>
              <div class="form-group">
                <label class="col-md-2 control-label">描述</label>
                <div class="col-md-10">


                  <div class="tabpanel mkeditor">
                    <ul class="nav nav-tabs" role="tablist">
                      <li role="presentation" class="active">
                        <a href="#mkeditor-editor" role="tab" data-toggle="tab">编辑</a>
                      </li>
                      <li role="presentation">
                        <a class="mkeditor-btn-view" href="#mkeditor-viewer" role="tab"
                           data-toggle="tab">预览</a>
                      </li>
                    </ul>
                    <div class="tab-content">
                      <div class="tab-pane active mkeditor-editor" id="mkeditor-editor"
                           role="tabpanel">

                        <div class="btn-group" role="group">

                          <button type="button" class="btn btn-default mkeditor-btn-bold">
                            <i class="fa fa-bold"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-italic">
                            <i class="fa fa-italic"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-link">
                            <i class="fa fa-link"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-quote">
                            <i class="fa fa-quote-left"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-code">
                            <i class="fa fa-code"></i>
                          </button>
                          <button id="mkeditor-ask-question" type="button"
                                  class="btn btn-default mkeditor-btn-img">
                            <i class="fa fa-image"></i>
                          </button>

                          <button type="button" class="btn btn-default mkeditor-btn-listol">
                            <i class="fa fa-list-ol"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-listul">
                            <i class="fa fa-list-ul"></i>
                          </button>
                        </div>
                        <div class="btn-group pull-right" role="group">
                          <a style="font-size:12px; color:#666; text-decoration:underline;"
                             href="/questions/764" target="_blank">
                            <i class="fa fa-question-circle"></i>Markdown 语法
                          </a>
                        </div>
                        <textarea name="content" class="content"
                                  min="0" max="20000"
                                  placeholder="推荐使用 Markdown 语法，至少输入 5 个字"></textarea>
                        <div class="help-block"></div>
                      </div>
                      <div class="tab-pane mkeditor-viewer markdown-body" id="mkeditor-viewer"
                           role="tabpanel">
                        <div></div>
                      </div>
                    </div>
                  </div>

                </div>
              </div>
              <div class="form-group">
                <label class="col-md-2 control-label">板块</label>
                <div class="col-md-10">
                  <div class="q-types" data-type="">
                  </div>
                </div>
              </div>


            </form>
          </div>
          <div class="modal-footer">
            <a type="button" class="submit-question btn btn-primary" href="/vip" target="_blank"
               style="background:#FFFFFF;color:#00CC99;border:none;float:left;padding-left:0;"><img
              src="https://static.shiyanlou.com/img/senior-vip-icon.png" alt=""> 加入高级会员获得助教答疑</a>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal">提交</button>
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade askquestion-modal" id="edit-question-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role=document>
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title">发帖</h4>
          </div>
          <div class="modal-body words-ctrl">
            <form class="form-horizontal" action="/questions/">
              <input name="_csrf_token" type=hidden
                     value="1483797676##818560cdc39a2ed99c488cf67125c1f53c60ad03">
              <div class="form-group">
                <label class="col-md-2 control-label">标题</label>
                <div class="col-md-10">
                  <input type="text" name="title" min="5" max="100" class="form-control"
                         placeholder="至少输入5个字" value="好心人可以告诉我怎么截屏吗。。。">
                  <span class="help-block"></span>
                </div>
              </div>
              <div class="form-group">
                <label class="col-md-2 control-label">描述</label>
                <div class="col-md-10">


                  <div class="tabpanel mkeditor">
                    <ul class="nav nav-tabs" role="tablist">
                      <li role="presentation" class="active">
                        <a href="#edit-question-editor" role="tab" data-toggle="tab">编辑</a>
                      </li>
                      <li role="presentation">
                        <a class="mkeditor-btn-view" href="#edit-question-viewer" role="tab"
                           data-toggle="tab">预览</a>
                      </li>
                    </ul>
                    <div class="tab-content">
                      <div class="tab-pane active mkeditor-editor" id="edit-question-editor"
                           role="tabpanel">

                        <div class="btn-group" role="group">

                          <button type="button" class="btn btn-default mkeditor-btn-bold">
                            <i class="fa fa-bold"></i>

                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-italic">
                            <i class="fa fa-italic"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-link">
                            <i class="fa fa-link"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-quote">
                            <i class="fa fa-quote-left"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-code">
                            <i class="fa fa-code"></i>
                          </button>
                          <button id="mkeditor-edit-question" type="button"
                                  class="btn btn-default mkeditor-btn-img">
                            <i class="fa fa-image"></i>
                          </button>

                          <button type="button" class="btn btn-default mkeditor-btn-listol">
                            <i class="fa fa-list-ol"></i>
                          </button>
                          <button type="button" class="btn btn-default mkeditor-btn-listul">
                            <i class="fa fa-list-ul"></i>
                          </button>
                        </div>
                        <div class="btn-group pull-right" role="group">
                          <a style="font-size:12px; color:#666; text-decoration:underline;"
                             href="/questions/764" target="_blank">
                            <i class="fa fa-question-circle"></i>Markdown 语法
                          </a>
                        </div>
                        <textarea name="content" class="content"
                                  min="0" max="20000"
                                  placeholder="推荐使用 Markdown 语法，至少输入 5 个字"></textarea>
                        <div class="help-block"></div>
                      </div>
                      <div class="tab-pane mkeditor-viewer markdown-body"
                           id="edit-question-viewer" role="tabpanel">
                        <div></div>
                      </div>
                    </div>
                  </div>

                </div>
              </div>
              <div class="form-group">
                <label class="col-md-2 control-label">板块</label>
                <div class="col-md-10">
                  <div class="q-types" data-type="1">
                  </div>
                </div>
              </div>


            </form>
          </div>
          <div class="modal-footer">
            <a type="button" class="submit-question btn btn-primary" href="/vip" target="_blank"
               style="background:#FFFFFF;color:#00CC99;border:none;float:left;padding-left:0;"><img
              src="https://static.shiyanlou.com/img/senior-vip-icon.png" alt=""> 加入高级会员获得助教答疑</a>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal">提交</button>
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade" id="delete-question-modal" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">确定删除</h4>
          </div>
          <div class="modal-body">
            <p>删除后不可恢复</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="btn btn-primary btn-confirm" data-dismiss="modal">确定</button>
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span
            aria-hidden="true">&times;</span></button>
          <div class="modal-body">
            <ul class="nav nav-tabs" role="tablist">
              <li role="presentation" class="active">
                <a href="#signin-form" aria-controls="signin-form" role="tab" data-toggle="tab">登录</a>
              </li>
              <li role="presentation">
                <a href="#signup-form" aria-controls="signup-form" role="tab" data-toggle="tab">注册</a>
              </li>
            </ul>
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane active" id="signin-form">
                <form action="/login" method="post">
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-envelope" style="margin:0;"></i>
                      </div>
                      <input type="email" name="login" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" name="password" class="form-control"
                             placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline verify-code-item" style="display:none;">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control"
                               placeholder="请输入验证码">
                      </div>
                    </div>
                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">
                  </div>
                  <div class="form-group remember-login">
                    <input name="remember" type="checkbox" value="y"> 下次自动登录
                    <a class="pull-right" href="../reset_password/index.html">忘记密码？</a>
                  </div>
                  <div class="form-group">
                    <input class="btn btn-primary" name="submit" type="submit" value="进入实验楼">
                  </div>
                  <div class="form-group widget-signin">
                    <span>快速登录</span>
                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                    <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                  </div>
                  <div class="form-group error-msg">
                    <div class="alert alert-danger" role="alert"></div>
                  </div>
                </form>
              </div>
              <div role="tabpanel" class="tab-pane" id="signup-form">
                <form action="/register" method="post">
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-envelope" style="margin:0;"></i>
                      </div>
                      <input type="email" name="email" class="form-control" placeholder="请输入邮箱">
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="input-group">
                      <div class="input-group-addon">
                        <i class="fa fa-lock" style="margin:0;"></i>
                      </div>
                      <input type="password" name="password" class="form-control"
                             placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control"
                               placeholder="请输入验证码">
                      </div>
                    </div>
                    <img class="verify-code" src="" source="https://www.shiyanlou.com/captcha.gif">
                  </div>
                  <div class="form-group">
                    <input class="btn btn-primary" name="submit" type="submit" value="注册">
                  </div>
                  <div class="form-group agree-privacy">
                    注册表示您已经同意我们的<a href="../privacy/index.html" target="_blank">隐私条款</a>
                  </div>
                  <div class="form-group widget-signup">
                    <span>快速注册</span>
                    <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                    <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                    <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                    <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                    <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                  </div>
                  <div class="form-group error-msg">
                    <div class="alert alert-danger" role="alert"></div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer1></footer1>
  </div>
</template>
<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import {send} from "../../static/js/comm";

    export default {
        name: 'showquest',
        data() {
            return {
                myquestlist: {},
                reportcomment: [],
                commentdict: {},
                user_id: localStorage.getItem('user_id'),
                quest_id: 0,
                content: '',
                pid: 0,
                diss_id: 0
            }
        },
        components: {
            header1: header1,
            footer1: footer1,

        }, mounted() {
            this.quest_id = this.$route.query.id;
            send('/api/richText/?report_id=' + this.quest_id, 'get').then((res) => {
                this.myquestlist = res.data.dataList
                this.getreport();
            });

        },
        methods: {
            addreport: function () {
                send('/api/submit/', 'post', {
                    'quest_id': this.$route.query.id,
                    'user_id': this.user_id,
                    'content': this.content,
                    'course_id': 0,
                    'pid': this.pid
                }).then((res) => {
                    if (res.data.code == 200) {
                        alert('评论成功')
                        this.getreport()
                    }
                })
            },
            getreport: function () {
                send('/api/submit/?quest_id=' + this.quest_id, 'get', {}).then((res) => {
                    this.reportcomment = res.data
                })
            },
            show: function (i) {
                $('#coummm').modal('show');
                this.commentdict['id'] = i._id

            },
            backWrite: function () {
                alert(this.commentdict.id)
                send('/api/submit/', 'post', {
                    'pid': this.commentdict.id,
                    'content': this.content,
                    'user_id': this.user_id,
                    "quest_id": this.quest_id,
                    'course_id': 0,

                }).then((res) => {
                    this.getreport()
                })
            },
        },
    }
</script>

<template>
  <div id="questions">
    <header1></header1>
    <div class="container layout layout-margin-top">


      <div class="row">
        <div class="col-md-9 layout-body">

          <div class="content">

            <ul class="nav nav-tabs question-types" role="tablist">


              <!--   <li role="presentation" class="active">
                   <a href="#all" aria-controls="all" role="tab" toggle="tab">全部</a>
                 </li>
   -->
              <!--              <li role="presentation">-->
              <!--                <a href="#course" aria-controls="course" role="tab" toggle="tab">课程问答</a>-->
              <!--              </li>-->

              <li role="presentation">
                <a href="#labreport" aria-controls="labreport" role="tab" toggle="tab">实验报告</a>
              </li>

              <li role="presentation">
                <a href="javascript:;" aria-controls="course" role="tab" toggle="tab"><span @click="getdiss(types)"
                                                                                            aria-controls="discussion"
                                                                                            role="tab"
                                                                                            toggle="tab">交流讨论</span>
                </a></li>

              <div class="question-sort">
                <!--                <li><a class="active" href="#newest">最新</a>-->
                <!--                  /-->
                <!--                  <a href="#hot">最热</a>-->
                <!--                </li>-->
              </div>
            </ul>
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane active">

                <ul class="row question-items" v-if="c==0">


                  <li class="question-item" v-for="(i,index) in reportList" :key="index">
                    <div class="col-md-10">
                      <div class="col-sm-2 question-item-author">


                        <div class="user-avatar ">
                          <a class="avatar" href="javascript:;" target="_blank">
                            <img :src="i.pic">
                          </a>

                        </div>

                      </div>

                      <div class="col-sm-10">
                        <h4>

                          <!-- <img src="../../static/img/topQuestion.png"> -->

                          <a class="question-item-title" href="">
                            <router-link :to="{'name':'ShowQuestions',query:{'id':i.id}}">{{i.report_title}}
                            </router-link>
                          </a>
                        </h4>
                        <div class="question-item-summary">


                          <!-- 实验报告用户名称,等级,发表时间 -->
                          <div class="user-username ">
                            <a class="avatar" href="javascript:;" target="_blank">
                              {{i.username}}
                            </a>
                            <span class="user-level">{{i.userlevel}}</span>
                          </div>


                          <span class="question-item-date">{{i.create_time}}</span>

                          最后回复 <span class="question-item-date">


      <!-- 最后评论用户,等级 -->
    <div class="user-username ">
        <a class="username" href="javascript:;" target="_blank">
        </a>
      <!--        <span class="user-level">L38</span>-->
    </div>
 </span>


                        </div>
                      </div>
                    </div>
                    <div class="col-md-2 question-item-rank">
                      <div class="question-item-answered">
                        <div>{{i.linknum}}</div>
                        <div>回复</div>
                      </div>
                      <div class="question-item-views">
                        <div>{{i.report_browse}}</div>
                        <div>
                          查看
                        </div>
                      </div>
                    </div>
                  </li>

                </ul>


                <ul class="row question-items" v-else-if="c==1">


                  <li class="question-item" v-for="(i,index) in disslist" :key="index">
                    <div class="col-md-10">
                      <div class="col-sm-2 question-item-author">


                        <div class="user-avatar ">
                          <a class="avatar" href="javascript:;" target="_blank">
                            <img :src="i.img">
                          </a>

                        </div>

                      </div>

                      <div class="col-sm-10">
                        <h4>

                          <!-- <img src="../../static/img/topQuestion.png"> -->

                          <a class="question-item-title" href="javascript:;">
                            <router-link :to="{'name':'Showdiscuss',query:{'id':i._id}}">{{i.title}}</router-link>
                          </a>

                        </h4>
                        <div class="question-item-summary">


                          <!-- 实验报告用户名称,等级,发表时间 -->
                          <div class="user-username ">
                            <a class="avatar" href="javascript:;" target="_blank">
                              {{i.username}}
                            </a>
                            <span class="user-level">{{i.userlevel}}</span>
                          </div>


                          <span class="question-item-date">{{i.create_time}}</span>

                          最后回复 <span class="question-item-date">


      <!-- 最后评论用户,等级 -->
    <div class="user-username ">
        <a class="username" href="javascript:;" target="_blank">
        </a>
    </div>
 </span>


                        </div>
                      </div>
                    </div>
                    <div class="col-md-2 question-item-rank">
                      <div class="question-item-answered">
                        <div>{{i.linknum}}</div>
                        <!--                        <div>回复</div>-->
                      </div>
                      <div class="question-item-views">
                        <div>{{i.report_browse}}</div>
                        <div>
                          <!--                          <router-link :to="{'name':'ShowQuestions',query:{'id':i.id}}">查看-->
                          <!--                          </router-link>-->
                        </div>
                      </div>
                    </div>
                  </li>

                </ul>


                <!--                <nav class="pagination-container">-->
                <!--                  <ul class="pagination">-->

                <!--                    <li class="disabled">-->
                <!--                      <a href="#" aria-label="Previous">-->
                <!--                        <span aria-hidden="true">上一页</span>-->
                <!--                      </a>-->
                <!--                    </li>-->


                <!--                    <li class="active">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=1&amp;area_type=all">1</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=2&amp;area_type=all">2</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=3&amp;area_type=all">3</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=4&amp;area_type=all">4</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=5&amp;area_type=all">5</a>-->
                <!--                    </li>-->


                <!--                    <li>-->
                <!--                      <a href='#'>...</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=547&amp;area_type=all">547</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a href="/questions/?sort=newest&amp;page=548&amp;area_type=all">548</a>-->
                <!--                    </li>-->


                <!--                    <li class="">-->
                <!--                      <a aria-label="Next" href="/questions/?sort=newest&amp;page=2&amp;area_type=all">-->
                <!--                        <span aria-hidden="true">下一页</span>-->
                <!--                      </a>-->
                <!--                    </li>-->

                <!--                  </ul>-->
                <!--                </nav>-->


              </div>
            </div>
          </div>

        </div>


        <right></right>


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

            <div><h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！</h4>
            </div>

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
              <input name="_csrf_token" type=hidden value="1483789088##bbf83c51243ab12daa94911c8865a65bdc66c4d8">
              <div class="form-group">
                <label class="col-md-2 control-label">标题</label>
                <div class="col-md-10">
                  <input type="text" name="title" min="5" max="100" class="form-control" v-model="title"
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
                        <a class="mkeditor-btn-view" href="#mkeditor-viewer" role="tab" data-toggle="tab">预览</a>
                      </li>
                    </ul>
                    <div class="tab-content">
                      <div class="tab-pane active mkeditor-editor" id="mkeditor-editor" role="tabpanel">

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
                          <button id="mkeditor-pickfile" type="button" class="btn btn-default mkeditor-btn-img">
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
                          <a style="font-size:12px; color:#666; text-decoration:underline;" href="/questions/764"
                             target="_blank">
                            <i class="fa fa-question-circle"></i>Markdown 语法
                          </a>
                        </div>
                        <textarea name="content" class="content"
                                  min="0" max="20000"
                                  placeholder="推荐使用 Markdown 语法，至少输入 5 个字" v-model="content"></textarea>
                        <div class="help-block"></div>
                      </div>
                      <div class="tab-pane mkeditor-viewer markdown-body" id="mkeditor-viewer" role="tabpanel">
                        <div></div>
                      </div>
                    </div>
                  </div>

                </div>
              </div>


            </form>
          </div>
          <div class="modal-footer">      <!--../../static/img/senior-vip-icon.png-->
            <a type="button" class="submit-question btn btn-primary" href="/vip" target="_blank"
               style="background:#FFFFFF;color:#00CC99;border:none;float:left;padding-left:0;"><img src="" alt="">
              加入高级会员获得助教答疑</a>
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal" @click="adddiscuss">
              发表讨论
            </button>
          </div>
        </div>
      </div>
    </div>


    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span>
          </button>
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
                      <input type="password" name="password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline verify-code-item" style="display:none;">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
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
                      <input type="password" name="password" class="form-control" placeholder="请输入密码">
                    </div>
                  </div>
                  <div class="form-inline">
                    <div class="form-group">
                      <div class="input-group">
                        <input type="text" name="captcha_v" class="form-control" placeholder="请输入验证码">
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
    import right from '@/components/right'
    import {send} from "../../static/js/comm";


    export default {
        name: 'questions',
        data: function () {
            return {
                reportList: [],
                disslist: [],
                title: '',
                types: 1,
                content: '',
                user_id: localStorage.getItem('user_id'),
                c: 0,
            }
        },
        components: {
            header1: header1,
            footer1: footer1,
            right: right,

        },
        mounted() {
            this.getreport()
        },
        methods: {
            getreport: function () {
                send('/api/richText/', 'get', {}).then((res) => {
                    if (res.data.code == 200) {
                        this.reportList = res.data.dataList
                    }
                })
            },
            shows: function () {
                if (this.user_id != null) {
                    $('#askquestion').modal('show');
                } else {
                    this.$router.push({'path': '/'})
                }
            },
            adddiscuss: function () {
                send('/api/dissubmit/', 'post', {
                    'user_id': this.user_id,
                    'title': this.title,
                    'content': this.content,
                    'types': this.types
                })
            },
            getdiss: function (types) {
                send('/api/dissubmit/?types=' + types, 'get').then((res) => {
                    this.c = 1;
                    this.disslist = res.data
                })
            }

        }
    }
</script>

<template>
  <div id="courseDetail">
    <header1></header1>
    <div class="container layout layout-margin-top">

      <ol class="breadcrumb">
        <li>
          <router-link :to="{'name':'course'}">全部课程
          </router-link>
        </li>

        <li>
          <router-link :to="{'name':'course',params:{'tid':courseData.tag_id}}">
            {{courseData.tag}}
            <!--            <a href="/courses/?tag=Linux">{{courseData.tag}}</a>-->
          </router-link>
        </li>

        <li class="active">
          <a href="/courses/1">
            {{courseData.title}}
          </a>
        </li>
      </ol>

      <div class="row">
        <div class="col-md-9 layout-body">


          <div class="side-image side-image-mobile">
            <img src="https://dn-simplecloud.shiyanlou.com/ncn1.jpg?imageView2/0/h/300">
          </div>
          <div class="content course-infobox">
            <div class="clearfix course-infobox-header">
              <h4 class="pull-left course-infobox-title">

                <span>{{courseData.title}}</span>

              </h4>
              <div class="pull-right course-infobox-follow" data-follow-url="/courses/1/follow"
                   data-unfollow-url="/courses/1/unfollow">
                <span class="course-infobox-followers">{{courseData.attention}}</span>
                <span>人关注</span>

                <i class="fa fa-star-o" data-next="/login?next=%2Fcourses%2F1"></i>

              </div>
            </div>
            <div class="clearfix course-infobox-body">
              <div class="course-infobox-content">
                <p>{{courseData.info}}</p>

              </div>

              <div class="course-infobox-progress">
                <!--                <div class="course-progress-new" v-for="(i,index) in sectionList" :key="index">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>-->
                <!--                <span>（0/{{sectionList.length}}）</span>-->
              </div>


              <div class="pull-right course-infobox-price">

              </div>

            </div>

            <div class="clearfix bootcamp-infobox">
              <div class="bootcamp-infobox-footer">

                <div class="col-md-3 bootcamp-infobox-msg">
                  <img src="../../static/img/bootcamp-course.png">
                  <div class="msg-desc"><span>4 个步骤详细的项目实验</span></div>
                  <img class="bootcamp-infobox-footer-plus" src="../../static/img/bootcamp-plus.png">
                </div>

                <div class="col-md-3 bootcamp-infobox-msg">
                  <img src="../../static/img/bootcamp-env.png">
                  <div class="msg-desc"><span>最新实用的实战技术</span></div>
                  <img class="bootcamp-infobox-footer-plus" src="../../static/img/bootcamp-plus.png">
                </div>
                <div class="col-md-3 bootcamp-infobox-msg">
                  <img src="../../static/img/bootcamp-qa.png">
                  <div class="msg-desc"><span>有问必答的实验助教</span></div>
                  <img class="bootcamp-infobox-footer-plus" src="../../static/img/bootcamp-equal.png">
                </div>


                <div class="col-md-3 bootcamp-infobox-msg bootcamp-infobox-buybox" v-show="showButtom">
                  <div v-show="showAllPrice==false">
                    {{priceList[0].level}}&nbsp;

                    <!--                    <div v-show="priceList[0].discount*1 <10">-->
                    <!--                      {{priceList[0].discount}}折-->
                    <!--                    </div>-->
                    <div class="original-price">￥{{priceList[0].discoun_price}}</div>
                    <a href="#" @click="showAllPrice=true">会员最低{{priceList[priceList.length-1].discount}}折</a>
                  </div>
                  <div v-for="(item,index) in  priceList" v-show="showAllPrice" :key="index">
                    {{item.level}}&nbsp;
                    <div v-show="item.discount*1 <10">
                      {{item.discount}}折
                    </div>
                    <div class="original-price">￥{{item.discoun_price}}</div>
                  </div>


                  <div class="member-price">

						<span class="member-price" data-container="body" data-toggle="popover" data-placement="top"
                  data-original-title="会员优惠" data-html="true" data-content="">
<!--              <a href="/vip" title="">会员最低5折</a>-->
            </span>

                  </div>

                  <div class="bootcamp-infobox-buy" @click="showBuy">
                    立即购买
                  </div>

                </div>

              </div>
            </div>

            <div class="clearfix course-infobox-footer">

              <div class="pull-right course-infobox-learned">{{courseData.learn}} 人学过</div>
            </div>

          </div>
          <div class="content">
            <ul class="nav nav-tabs" role="tablist">

              <li role="presentation" class="active">
                <a href="#labs" aria-controls="labs" role="tab" data-toggle="tab">实验列表</a>
              </li>

              <li role="presentation">
                <a href="#comments" class="stat-event" aria-controls="comments" role="tab"
                   data-stat="course_comment" data-toggle="tab" @click="getcomment">课程评论</a>
              </li>
              <li role="presentation">
                <a href="#reports" class="stat-event" data-stat="course_report" aria-controls="reports"
                   role="tab" data-toggle="tab">实验报告</a>
              </li>
              <!--              <li role="presentation">-->
              <!--                <a href="#questions" class="stat-event" data-stat="course_question"-->
              <!--                   aria-controls="questions" role="tab" data-toggle="tab">实验问答</a>-->
              <!--              </li>-->
            </ul>
            <div class="tab-content">
              <!--错误-->
              <div role="tabpanel" class="tab-pane active" id="labs">


                <!--                <div class="lab-item">
                                  <h4 class="lab-item-title">第1章:Linux 系统简介</h4>
                                </div>-->

                <div class="lab-item change_curse" v-for="(item,index) in sectionList" :key="index">
                  <!-- <button type="button" class="btn btn-default btn-lg btn-block"> -->
                  <div class="lab-item-status" v-show="lList.indexOf(item.id)!=-1">

                    <img src="../../static/img/lab-not-ok.png">

                  </div>


                  <div class="lab-item-index" style="float: left" @click="play(item)">第{{item.sort}}章</div>
                  <div class="lab-item-title" data-toggle="tooltip" data-placement="bottom"
                       :title="item.section">
                  </div>
                  <div class="pull-right lab-item-ctrl">

                  </div>
                  <div class="pull-right lab-item-ctrl">
                    {{item.section}}
                  </div>


                  <!-- </button> -->
                </div>


              </div>
              <div role="tabpanel" class="tab-pane course-comment" id="comments">
                <div class="comment-box">
                  <div class="comment-form">

                    <div class="comment-form-unlogin" v-show="showButtom==true">
                      请购买后发表评论
                    </div>
                    <div v-show="showButtom==false">
                      <textarea name="" id="" cols="120" rows="10" v-model="content"></textarea>
                      <div>
                        <div
                          :style="{'float':'right','text-align':'right','padding-right':'10px','border-radius':'25px'}">
                          <button
                            :style="{'border-radius':'25px','background':'#7EAB1E'}" type="submit" value="评论"
                            width="80px" @click="addcomment">发表评论
                          </button>
                        </div>
                      </div>
                    </div>

                  </div>
                  <div class="comment-title">最新评论</div>
                  <div class="comment-list" id="news-lis">

                    <div v-for="(i,index) in commentlist" :style="{'text-align':'left'}" :key="index"
                         v-show="index < nums">


                      <div class="user-avatar report-item-avatar">
                        <a class="avatar" href="#" target="_blank">
                          <img
                            :src="i.img">
                        </a>{{i.username}} <span
                        :style="{'font-size':'18px' ,'color':'#d39614'}"> </span>


                      </div>

                      <p><br><span :style="{'font-size':'18px' ,'color':'#000'}">{{i.content}}</span></p>
                      <p v-if="i.back_username==''">{{i.create_time}}&nbsp;&nbsp;&nbsp;来自:{{courseData.title}}</p>
                      <p v-else>{{i.create_time}}&nbsp;&nbsp;&nbsp;回复:{{i.back_username}}</p>

                      <div :style="{'text-align':'right'}"><img src="../../static/img/下载.png" alt="">
                        <span @click="show(i)">回复</span>
                        <hr style="size:3px">
                      </div>

                    </div>
                    <div v-for="(i,index) in commentlist" :style="{'text-align':'left'}" :key="index"
                         v-show="index <= commentlist.lenght">
                      <p>{{i.username}} <span :style="{'font-size':'18px' ,'color':'#d39614'}"> {{i.userlevel}}</span>
                      </p>
                      <div style="width:100px; height:100px; border-radius:50px; overflow: hidden;"><img :src="i.img"
                                                                                                         alt=""></div>
                      <p><br><span :style="{'font-size':'18px' ,'color':'#000'}">{{i.content}}</span></p>
                      <p v-if="i.back_username==''">{{i.create_time}}&nbsp;&nbsp;&nbsp;来自:{{courseData.title}}</p>
                      <p v-else>{{i.create_time}}&nbsp;&nbsp;&nbsp;回复:{{i.back_username}}</p>

                      <div :style="{'text-align':'right'}"><img src="../../static/img/下载.png" alt="">
                        <span @click="show(i)">回复</span>
                        <hr style="size:3px">
                      </div>

                    </div>
                  </div>

                  <div class="pagination-container">
                    <button @click="showMore">{{txt}}</button>
                  </div>


                </div>
              </div>
              <div role="tabpanel" class="tab-pane" id="reports">
                <!--                <span class="lab-id active" data-lab-id="None">全部</span>-->
                <!--                <span class="lab-id" data-lab-id="1" v-for="item in sectionList">第{{item.sort}}节</span>-->
                <div class="report-owner">
                  <span class="owner-list" data-user-id="">我的报告</span> / <span class="owner-list active"
                                                                               data-user-id="None">所有报告</span>
                  <div class="row">
                    <div class="row report-items">

                      <div class="col-md-3 report-item clearfix" v-for="item in reportList">
                        <a :href='"/ShowQuestions?id="+item.id'>
                          <div class="report-item-course">
                            {{item.report_title}}
                          </div>
                          <div class="report-item-lab">章节： {{item.section_name}}</div>
                          <div class="pull-right report-item-update">
                            {{item.create_time}}
                          </div>
                          <div class="tags">
                            <!--                            <span class="tag tag-primary"><a :href='"/ShowQuestions?id="+item.id'>查看详情</a></span>-->
                          </div>
                          <div class="report-item-count">
                            <span>{{item.count}} 字</span>
                            <div class="report-item-arrow">
                              <div class="report-item-arrow-line"></div>
                            </div>
                          </div>

                          <!--
                          <div class="report-item-benchmark">
                              <img src="../../img/labreport-evaluate-A.png">
                          </div>-->

                        </a>
                        <div class="col-xs-8">
                          <div class="report-item-author">


                            <div class="user-avatar report-item-avatar">
                              <a class="avatar" href="#" target="_blank">
                                <img :src="item.pic">
                              </a>

                              <a class="member-icon" href="#" target="_blank">
                              </a>

                            </div>


                            <div class="user-username ">
                              <a class="username" href="#" target="_blank">
                                {{item.username}}
                                <br>
                              </a>
                              <br>
                            </div>

                          </div>
                        </div>
                        <div class="col-xs-4">
                          <div class="pull-right report-item-comments">

                          </div>

                        </div>
                      </div>


                    </div>


                  </div>

                  <select v-model="sid" style="float: left">
                    <option v-for="item in sectionList" :value="item.id" v-show="lList.indexOf(item.id)!=-1">
                      {{item.section}}
                    </option>
                  </select>
                  (提示：可选学习过的章节写实验报告)
                  <fuwenben v-on:listentochildevents='showMesfromchild' v-if="this.sid >0"></fuwenben>

                </div>

                <div class="row report-items"></div>
                <div class="pagination-container"></div>
              </div>
              <div role="tabpanel" class="tab-pane" id="questions">
                <a class="btn btn-success" data-toggle="modal" data-target="#askquestion">我要提问</a>
                <hr>
                <ul class="row question-items"></ul>
                <div class="pagination-container"></div>
              </div>
            </div>
          </div>


        </div>
        <div class="col-md-3 layout-side">

          <div class="side-image side-image-pc">
            <!--            <img src="../../static/img/ncn1.jpg?imageView2/0/h/300">-->
          </div>


          <div class="sidebox mooc-teacher">
            <div class="sidebox-header mooc-header">
              <h4 class="sidebox-title">课程教师</h4>
            </div>
            <div class="sidebox-body mooc-content">
              <a href="/user/20406" target="_blank">
                <img :src="teacher.pic">
              </a>
              <div class="mooc-info">
                <div class="name"><strong>{{teacher.name}}</strong></div>

                <div class="courses">共发布过<strong>{{teacher.num}}</strong>门课程</div>
              </div>
              <div class="mooc-extra-info">
                <div class="word long-paragraph">
                  {{teacher.info}}
                </div>
              </div>
            </div>
            <div class="sidebox-footer mooc-footer">
              <!--              <a href="/teacher/20406" target="_blank">查看老师的所有课程 ></a>-->
            </div>
          </div>

          <div class="sidebox">

            <div class="sidebox-header">
              <h4 class="sidebox-title">推荐课程</h4>
            </div>
            <div class="sidebox-body course-content side-list-body" style="text-align: left">
              <a :href='"/courseDetail?id="+item.id' v-for="item in rList"><img
                style="width:25px;height:25px"
                :src="item.pic">
                {{item.title}}</a>
            </div>

          </div>


        </div>
      </div>
    </div>
    <div class="modal fade" id="invite-user" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span
              aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title">邀请好友，双方都可获赠实验豆！</h4>
          </div>
          <div class="modal-body">

            <div>
              <h4><a href="#sign-modal" data-toggle="modal" data-sign="signin">登录</a>后邀请好友注册，您和好友将分别获赠3个实验豆！
              </h4>
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
            <button type="button" class="close" data-dismiss="modal"><span
              aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
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
                                  placeholder="推荐使用 Markdown 语法，至少输入 5 个字" v-model="content"></textarea>
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
            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal" @click="backWrite">提交
            </button>
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
                     value="1483794941##be4fb68b276c5f7cb970936cb25985cd53b943d1">
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
            <!--            <a type="button" class="submit-question btn btn-primary" href="/vip" target="_blank"-->
            <!--               style="background:#FFFFFF;color:#00CC99;border:none;float:left;padding-left:0;"><img-->
            <!--              src="../../static/img/senior-vip-icon.png" alt=""> 加入高级会员获得助教答疑</a>-->
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
            <button type="button" class="submit-question btn btn-primary" data-dismiss="modal">提交</button>
          </div>
        </div>
      </div>
    </div>

    <div class="modal fade" id="start-newlab">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h3>开始新实验</h3>
          </div>
          <div class="modal-body" style="text-align:center">
            <p> 一个实验正在进行，是否停止它，开始新实验？</p>

          </div>
          <div class="modal-footer" style="margin-top:0px">

            <button class="btn" data-dismiss="modal" aria-hidden="true">关闭</button>
            <a class="btn btn-primary start-newlab-confirm">确定</a>

          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>
    <div class="modal fade" id="start-evaluation-course">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h3>开始评估课实验</h3>
          </div>
          <div class="modal-body">
            <div>
              <p>为了让评估结果更加准确，请注意以下操作：</p>
              <ul>
                <li>完成实验后点击「停止实验」按钮</li>
                <li>将代码提交到代码库</li>
                <li>尽可能详尽的撰写实验报告</li>
                <li>尽可能在实验操作的关键步骤截图</li>
                <li>尽可能减少无用操作</li>
                <li>尽可能高效的利用内存/CPU资源</li>
              </ul>
              <p>评估课还在不断完善中，我们真挚希望你能通过我们提供的这个平台，找到更好的发展机会。</p>
            </div>
            <br>
            <div class="start-newlab"></div>
          </div>
          <div class="modal-footer">
            <button class="btn" data-dismiss="modal" aria-hidden="true">关闭</button>
            <a class="btn btn-primary start-confirm">确定</a>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>
    <div class="modal fade" id="vip-startlab-modal">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
            <h3>开始实验</h3>
          </div>
          <div class="modal-body">
            <div class="start-newlab"></div>
            <br>
            <div class="text-center vip-vm">
              <a class="btn btn-default btn-lg newvm">创建新环境</a>

            </div>
            <br>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
    </div>
    <div class="modal fade" id="bean-course-modal" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span
              aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title">激活项目课：Linux 基础入门（新版）</h4>
          </div>
          <div class="modal-body">
            <div style="font-size:14px; font-weight:thin;">
              要在实验楼愉快地学习，先要熟练地使用 Linux，本实验介绍 Linux 基本操作，shell 环境下的常用命令。
            </div>
            <div style="margin:36px 0 18px; font-size:16px; font-weight:bold;">
              您有 <span style="color:#f66;"><strong></strong></span> 个实验豆，激活本课程需要消耗 <span
              style="color:#f66;"><strong>0</strong></span> 个实验豆！
            </div>
            <div style="color:#84B61A; font-size:14px; font-weight:bold;">激活后可不限次数学习本课。<a href="/faq#shiyandou"
                                                                                          style="font-weight:normal;"
                                                                                          target="_blank">如何获得实验豆？</a>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>

            <a class="btn btn-primary getshiyandou" href="/faq#shiyandou" target="_blank"
               data-dismiss="modal">获取实验豆</a>

          </div>
        </div>
      </div>
    </div>


    <div class="modal fade" id="paid-modal" tabindex="-1" role="dialog" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h4 class="modal-title">购买课程</h4>

          </div>
          <div class="modal-body">
            <div class="vip-modal-item ">
              <div class="vip-modal-item-header">
                <div class="btn btn-default navbar-btn" @click="useCode=true" v-if="useCode==false">点击使用优惠券</div>
                <div class="btn btn-default navbar-btn" @click="useCode=false" v-if="useCode==true">暂不使用优惠券</div>
              </div>
              <div class="vip-modal-item-body">
                <div class="input-group" v-show="useCode==true">
                  <div v-show="myCoupons.length==0">
                    您还没有优惠券,
                    <router-link class="" :to="{'name':'userCenter'}">点击去用户中心领取优惠券</router-link>
                  </div>
                  <div class="alert-message" v-for="(item,index) in myCoupons" :key="index" v-if='useCode==true'>
                  <span class="tag tag-primary"
                        style="background: #0ace9d 100px"
                        @click="selectCoupon(item.code)"> <input
                    type="radio" :value="item.code"
                    v-model="coupon">{{item.name}}满￥{{item.condition}}减{{item.money}}</span>
                  </div>

                </div>
              </div>
            </div>


            <div class="vip-modal-item">
              <div class="vip-modal-item-header"><span>
                <div class="btn btn-default navbar-btn" @click="useScore=true" v-if="useScore==false">点击使用积分</div>
                <div class="btn btn-default navbar-btn" @click="useScore=false"
                     v-if="useScore==true">暂不不使用积分</div></span>
              </div>
              <div class="vip-modal-item-body">
                <div class="consume-beans" v-show="useScore==true">
                  <input type="text" class="form-control phone-number"
                         value="" placeholder="最高使用100个积分" v-model="num">
                </div>
              </div>
            </div>

            <div class="vip-modal-item">
              <div class="vip-modal-item-header">支付方式: <br>
                <img src="../../static/img/Snipaste_2019-10-17_10-29-45.png" height="50" width="100"/>
              </div>

            </div>
          </div>
          <div class="modal-body vip-modal-qrcode" style="display:none;">

            <div class="vip-wx-price">付款：<span></span></div>
            <div class="vip-wx-qrcode"></div>
            <a class="vip-wx-method" href="javascript:;">更换支付方式</a>
          </div>
          <div class="modal-footer">
            <div class="pull-left real-price">
              <div>
                <div style="float:left"><strong class="last-price">
                  <div v-for="(item,index) in  priceList" :key="index" v-show="item.type==userInfo.level.level">
                    <span>付款：</span><strong>￥</strong>{{item.discoun_price}}
                  </div>
                </strong>
                </div>
                <br class="__web-inspector-hide-shortcut__">

              </div>


            </div>
            <div class="pull-right pay-btn">
              <a class="btn btn-warning" href="#" @click="buyMember()" v-show="f==false">确认购买</a>
              <a class="btn btn-warning" :href="payUrl" v-show="f">去支付</a>

              <!--              <input type="checkbox" checked>-->
              <!--              <span>同意<a href="/terms" target="_blank">会员服务条款</a></span>-->
            </div>
          </div>
        </div>
      </div>
    </div>

    <footer1></footer1>
  </div>


</template>

<script>
    import {send, sendToken} from '../../static/js/comm'
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'
    import right from '@/components/right'
    import fuwenben from '@/components/fuwenben'
    import Index from "./index";
    import axios from "axios";


    export default {
        name: "courseDetail",
        data: function () {
            return {
                user_id: localStorage.getItem('user_id'),
                cid: 0,
                courseData: {},
                commentlist: [],
                commenttdict: {},
                sectionList: [],
                priceList: [{'level': 0}],
                teacher: {},
                myCoupons: [],
                f: false,
                useScore: false,
                useCode: false,
                coupon_code: '',
                integral: 0,
                num: 0,
                money: 0,
                content: '',
                userInfo: {'level': {'level': 0}},
                addForm: {},
                amount: 0,
                payUrl: '',
                coupon: '',
                price: 9999,
                pay_type: 1,
                preferential_way: 0,
                showButtom: false,
                showAllPrice: false,
                nums: 2,
                isShow: true,
                txt: '点击查看更多',
                rList: [],
                lList: [],
                sid: 0,
                reportList: [],
                commentdict: {},
                lcList: [],
                pid: 0

            }
        },


        mounted() {
            this.cid = this.$route.query.id;
            if (localStorage.getItem('user_id') != undefined) {
                send('/api/recommend/?user_id=' + localStorage.getItem('user_id'), 'get').then((res) => {
                    this.rList = res.data.courseList
                });
                sendToken('/api/user/?user_id=' + localStorage.getItem('user_id'), 'get').then((res) => {
                    if (res.data.code == 200) {
                        this.userInfo = res.data.userInfo;
                        this.lList = res.data.lList;
                        this.lcList = res.data.lcList;
                    } else {
                        alert(res.data.message)
                    }
                });
            }
            send('/api/admin01/course/?id=' + this.cid, 'get').then((res) => {
                if (res.data.code == 200) {
                    this.courseData = res.data.dataList;
                    send('/api/admin01/teacher/?id=' + res.data.dataList.teacher_id, 'get').then((res) => {
                        this.teacher = res.data.dataList
                    });

                } else {
                    // this.$router.push({name: 'course'})
                }
            }).catch((err) => {
            });
            send('/api/admin01/section/?course_id=' + this.cid, 'get').then((res) => {
                this.sectionList = res.data.dataList
            });
            this.getcomment();
            if (localStorage.getItem('user_id') != undefined) {
                send('/api/courseOrder/', 'put', {
                    'user_id': localStorage.getItem('user_id'),
                    'course_id': this.cid
                }).then((res) => {
                    if (res.data.dataList.length < 1) {
                        this.showButtom = true
                    }
                })

            } else {
                this.showButtom = true
            }
            send('/api/admin01/price/?course_id=' + this.cid, 'get').then((res) => {
                if (res.data.code == 200) {
                    this.priceList = res.data.dataList;

                } else {
                    // this.$router.push({name: 'course'})
                }
            }).catch((err) => {
                // this.$router.push({name: 'course'})
            });
            send('/api/richText/?course=' + this.cid, 'get').then((res) => {
                if (res.data.code == 200) {
                    this.reportList = res.data.dataList
                }
            })
        },
        methods: {
            showMesfromchild(data) {
                data['section_id'] = this.sid;
                data['user_id'] = localStorage.getItem('user_id');
                data['course_id'] = this.cid;
                sendToken('/api/richText/', 'post', data).then((res) => {
                    if (res.data.code == 200) {
                        alert('发布成功')
                        send('/api/richText/?course=' + this.cid, 'get').then((res) => {
                            if (res.data.code == 200) {
                                this.reportList = res.data.dataList
                            }
                        })
                        this.sid = 0
                    } else {
                        alert('发布失败')
                    }
                }).catch((error) => {
                    alert('网络错误，请稍后重试')
                })
            },
            showBuy: function () {
                if (localStorage.getItem('user_id') != undefined) {
                    $('#paid-modal').modal('show')
                    send('/api/mycoupon/?user_id=' + localStorage.getItem('user_id') + '&course_id=' + this.cid, 'get').then((res) => {
                        if (res.data.code == 200) {
                            this.myCoupons = res.data.couponList
                        }
                    })
                    // $('#charge-course-modal').modal('show')
                } else {
                    $('#sign-modal').modal('show')
                }
            },
            play: function (item) {

                if (this.courseData.member == 0 || this.showButtom == false) {
                    if (this.lList.indexOf(item.id) != -1) {
                        this.$router.push({name: 'video', params: {'video': item.video,}})

                    } else {
                        send('/api/uploadcourse/', 'put', {
                            'section_id': item.id,
                            'course_id': this.cid,
                            'user_id': localStorage.getItem('user_id')
                        }).then((res) => {
                            this.$router.push({name: 'video', params: {'video': item.video,}})

                        })
                    }
                } else {
                    this.showBuy()
                }
            },
            selectCoupon: function () {

            },
            buyMember: function () {
                // alert(this.money)
                if (this.useScore == false || this.num == 0) {
                    this.num = 0;
                    this.useScore = false;
                    this.preferential_way = 1
                }
                if (this.useCode == false || this.coupon == '') {
                    this.coupon = '';
                    this.preferential_way = 2;
                    this.useCode = false;

                }
                if (this.useCode == false && this.useScore == false) {
                    this.coupon = '';
                    this.num = 0;
                    this.preferential_way = 0


                }
                send('/api/courseOrder/', 'post', {
                    'uid': this.userInfo.id,
                    'cid': this.cid,
                    'num': this.num,
                    'pay_type': this.pay_type,
                    'coupon': this.coupon,
                    'preferential_way': this.preferential_way
                }).then((res) => {
                    if (res.data.code == 200) {
                        send('/api/pay/?courseOrder_sn=' + res.data.courseOrder_sn, 'get').then(
                        ).then((res) => {
                            if (res.data.code == 200) {
                                this.f = true;
                                this.payUrl=res.data.path;
                                window.location.href = res.data.path;
                            }
                        })
                    } else {
                        alert('订单提交失败')
                    }
                })
            },
            addcomment: function () {
                if (this.content == '') {
                    alert('请输入正确内容')
                } else {
                    send('/api/submit/', 'post', {
                        'content': this.content,
                        'user_id': localStorage.getItem('user_id'),
                        'pid': this.pid,
                        'course_id': this.cid
                    }).then((res) => {
                        if (res.data.code == 200) {
                            alert('评论成功')
                            this.content = ''
                            this.getcomment()
                        } else {
                            alert(res.data.message)
                        }
                    })

                }
            },
            getcomment: function () {  //获取评论列表
                send('/api/submit/?course_id=' + this.cid, 'get').then((res) => {
                    this.commentlist = res.data
                })
            },
            show: function (i) {
                $('#coummm').modal('show');
                this.commentdict['_id'] = i._id

            },
            backWrite: function () {
                send('/api/submit/', 'post', {
                    'pid': this.commentdict._id,
                    'content': this.content,
                    'user_id': this.user_id,
                    "course_id": this.cid
                }).then((res) => {
                    this.getcomment()
                    this.content = ''
                    alert('评论成功')
                })
            },
            showMore: function () {
                this.isShow = !this.isShow;
                this.nums = this.isShow ? 2 : this.commentlist.length;
                this.txt = this.isShow ? '点击查看更多' : '收起'
            }

        },
        components: {
            // Index,
            right: right,
            header1: header1,
            footer1: footer1,
            fuwenben: fuwenben
        },
    }
</script>


<style scoped>

</style>

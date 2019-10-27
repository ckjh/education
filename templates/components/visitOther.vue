<template>
  <div id="visitOther">
    <header1></header1>
    <div class="userinfo-banner layout-no-margin-top">
      <div class="container layout">
        <div class="row">
          <div class="col-md-9 clearfix">
            <div class="pull-left userinfo-banner-avatar">
              <div class="user-avatar ">
                <a class="avatar" href="#" target="_blank">
                  <img :src="userInfo.img">
                </a>
                <a class="member-icon" href="../../vip/index.html" target="_blank">
                  <img src="
            ../../static/img/vip-icon.png
          ">
                </a>
              </div>
            </div>
            <div class="pull-left userinfo-banner-details">
              <div class="userinfo-banner-meta">
                <div class="user-username ">
                  <a class="username" href="#" target="_blank">
                    {{userInfo.username}}
                  </a>
                  <span class="user-level">{{level_name}}</span>
                </div>
              </div>
              <div class="userinfo-banner-status">
                <span>剩余积分:{{userInfo.integral}}</span>
                <span>我的邀请码:{{userInfo.invitation_code}}</span>
              </div>
            </div>
          </div>
          <div class="col-md-3 userinfo-banner-labinfo">
            <div class="userinfo-banner-level">
              <img src="../../static/img/lou-level.png">
              <div class="userinfo-current-level"><span>195</span> 楼</div>
              <div class="userinfo-level-more" data-toggle="tooltip" data-placement="bottom"
                   title="在实验环境中动手输入代码或命令时才计入有效学习时间">

                距 196 楼还需 16 分钟有效学习时间
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container layout">
      <div class="row">
        <div class="col-md-9 layout-body">
          <div class="content" role="tabpanel">
            <ul class="nav nav-tabs" rolw="tablist">
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('course','a')">实验课程</a>
              </li>
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('report')">实验报告</a>
              </li>
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('comment')">实验讨论</a>
              </li>
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('coupon')">优惠券</a>
              </li>
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('Orders')">订单</a>
              </li>
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('SiteMessage')">站内信</a>
              </li>
              <li role="presentation">
                <a href="#" role="tab" @click="showWhat('SetUp')">基本信息设置</a>
              </li>
              <!---->
            </ul>
            <div class="tab-content">
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='course'}" style="float: left">
                <div class="row">
                  <div class="col-md-12" style="text-align: left">
                    <a>
                      <span href="#" :class="{'label':true,'label-success':true}"
                            @click="showWhat('course','l')">学过的</span>
                    </a>
                    <a href="#">
                      <span :class="{'label':true,'label-success':true}" @click="showWhat('course','a')">关注的</span>
                    </a>
                  </div>

                  <div class="col-md-4 col-sm-6  course" v-for="item in clist" v-show="whatS=='a'">
                    <a class="course-box" :href='"/courseDetail?id="+item.id'>
                      <div class="sign-box">
                      </div>
                      <div class="course-img">
                        <img
                          :src="item.pic">
                      </div>
                      <!---->
                      <div class="course-body">
                                            <span class="course-title" data-toggle="tooltip" data-placement="bottom"
                                            >{{item.title}}</span>
                      </div>
                      <!--                      <div class="course-footer">-->
                      <!--    			<span class="course-per-num pull-left">-->
                      <!--                    <i class="fa fa-users"></i>-->
                      <!--{{item.learn}}-->
                      <!--    			</span>-->
                      <!--                      </div>-->
                    </a>
                  </div>
                  <div class="col-md-4 col-sm-6  course" v-for="item in learnList" v-show="whatS=='l'">
                    <a class="course-box" :href='"/courseDetail?id="+item.course'>
                      <div class="sign-box">
                      </div>
                      <div class="course-img">
                        <img
                          :src="item.pic">
                      </div>
                      <!---->
                      <div class="course-body">
                                            <span class="course-title" data-toggle="tooltip" data-placement="bottom"
                                            >课程:{{item.course_name}}</span>
                        <span class="course-title" data-toggle="tooltip" data-placement="bottom"
                        >章节:{{item.section_name}}</span>
                      </div>

                    </a>
                  </div>
                </div>
              </div>
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='comment'}">
                <div class="row">
                  <div class="col-md-12">
                    <a>
                      <span class="label label-success">话题</span>
                    </a>
                    <a href="/user/13/answers">
                      <span class="label label-default">回复</span>
                    </a>
                    <a href="/user/13/favorite">
                      <span class="label label-default">收藏</span>
                    </a>
                  </div>
                </div>
                <ul class="row question-items">
                  <li class="question-item">
                    <div class="col-md-10">
                      <div class="col-sm-2 question-item-author">


                        <div class="user-avatar ">
                          <a class="avatar" href="/user/13" target="_blank">
                            <img
                              src="https://dn-simplecloud.shiyanlou.com/gravatarc51ce410c124a10e0db5e4b97fc2af39.png?v=1439957390221&amp;imageView2/1/w/200/h/200">
                          </a>

                          <a class="member-icon" href="/vip" target="_blank">

                            <img src="
            ../../static/img/vip-icon.png
          ">

                          </a>

                        </div>

                      </div>
                      <div class="col-sm-10">
                        <h4>

                          <a class="question-item-title" href="../../questions/show.html" target="_blank">
                            实验楼高级会员：增加会员课程助教答疑服务和训练营5折优惠</a>

                        </h4>
                        <div class="question-item-summary">


                          <div class="user-username ">
                            <a class="username" href="/user/13" target="_blank">

                              石头山


                            </a>
                            <span class="user-level">L195</span>
                          </div>


                          <span class="question-item-date">2016-12-16 12:49</span>

                          最后回复 <span class="question-item-date">



    <div class="user-username ">
        <a class="username" href="/user/3858" target="_blank">

                Cloud君


        </a>
        <span class="user-level">L28</span>
    </div>
 </span>


                        </div>
                      </div>
                    </div>
                    <div class="col-md-2 question-item-rank">
                      <div class="question-item-answered">
                        <div>1</div>
                        <div>回复</div>
                      </div>
                      <div class="question-item-views">
                        <div>47</div>
                        <div>查看</div>
                      </div>
                    </div>
                  </li>
                </ul>
                <nav class="pagination-container">
                  <ul class="pagination">

                    <li class="disabled">
                      <a href="#" aria-label="Previous">
                        <span aria-hidden="true">上一页</span>
                      </a>
                    </li>


                    <li class="active">
                      <a href="/user/13/questions?page=1">1</a>
                    </li>


                    <li class="">
                      <a href="/user/13/questions?page=2">2</a>
                    </li>


                    <li class="">
                      <a aria-label="Next" href="/user/13/questions?page=2">
                        <span aria-hidden="true">下一页</span>
                      </a>
                    </li>

                  </ul>
                </nav><!---->


              </div>
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='report'}"
              >
                <div class="row">
                  <div class="row report-items">

                    <div class="col-md-3 report-item clearfix">
                      <a href="reports_show.html">
                        <div class="report-item-course">


                          新手指南之玩转实验楼
                        </div>
                        <div class="report-item-lab">Hello World!</div>
                        <div class="tags">


                          <span class="tag tag-primary">C/C++</span>


                        </div>
                        <div class="report-item-count">
                          <span>719 字</span>
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
                            <a class="avatar" href="/user/13" target="_blank">
                              <img
                                src="https://dn-simplecloud.shiyanlou.com/gravatarc51ce410c124a10e0db5e4b97fc2af39.png?v=1439957390221&amp;imageView2/1/w/200/h/200">
                            </a>

                            <a class="member-icon" href="/vip" target="_blank">

                              <img src="
            ../../static/img/vip-icon.png
          ">

                            </a>

                          </div>


                          <div class="user-username ">
                            <a class="username" href="/user/13" target="_blank">

                              石头山


                            </a>
                            <span class="user-level">L195</span>
                          </div>

                        </div>
                      </div>
                      <div class="col-xs-4">
                        <div class="pull-right report-item-comments">
                          <i class="fa fa-comments-o"></i>
                          1
                        </div>
                        <div class="pull-right report-item-update">
                          2016-12-27 08:41
                        </div>
                      </div>
                    </div>


                  </div>


                </div>
              </div>
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='coupon'}"
              >
                <div class="row">
                  <div class="row report-items">
                    <div class="cou">
                      <div class="coupon coupon-wave-left coupon-yellow" v-for="(i,index) in coupons" :key="index">
                        <div class="coupon-info coupon-hole coupon-info-right-dashed">
                          <div class="coupon-price">&yen;{{i.money}}</div>
                          <div class="coupon-desc">满{{i.condition}}元使用</div>
                          <div class="coupon-expiry-date">有效期：{{i.end_time}}</div>
                        </div>
                        <div
                          :class="{'coupon-get':true,'coupon-get-already':myCouponID.indexOf(i.id)!=-1}"
                        ><a href="#" @click="getIt(i.id)" :class="{btn:true, disabled:myCouponID.indexOf(i.id)!=-1}">立即领取</a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='SiteMessage'}">
                <div class="row">
                  <div class="row report-items">
                    <div class=" report-item clearfix" style="text-align: left" v-for="item in myMessage">
                      <div class="report-item-course" style="float: left">
                      </div>
                      <div class="tags" style="text-align: left">
                        <span class="tag"><h2>{{item.title}}</h2></span>
                        <br>
                        <span class="tag tag-primary">日期:{{item.create_time}}</span>
                        <span class="tag tag-primary" v-if="item.status==1">已查看</span>
                        <span class="tag tag-primary" v-if="item.status==0">未查看</span>
                        <br>
                        <span class="tag tag-primary"><a href="#" @click="showdetail(item)"> 查看详情</a></span>
                        <br>
                      </div>
                      <div class="col-xs-8">
                        <div class="report-item-author">
                          <div class="user-username " style="text-align: left">
                            <!--                            <span class="user-level">订单生成时间 :{{item.create_time}}<br>流水号:{{item.code}}<br>订单号:{{item.order_sn}}<br></span>-->
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='Orders'}">
                <div class="row">
                  <div class="row report-items">
                    <div class=" report-item clearfix" style="text-align: left" v-for="item in myOrders">
                      <div class="report-item-course" style="float: left">

                      </div>
                      <div class="tags" style="text-align: left">
                        <span class="tag"><h2>会员类型:{{item.level_name}}</h2></span>
                        <br>
                        <span class="tag tag-primary">订单金额:{{item.amount}}</span>
                        <br>

                        <span class="tag tag-primary">开通时长:{{item.time}}月</span>
                        <br>

                        <span class="tag tag-primary" v-if="item.pay_type==1">支付方式:支付宝</span>
                        <br>

                        <span class="tag tag-primary" v-if="item.num>0">使用的积分{{item.num}}</span>
                        <br>

                      </div>
                      <div class="col-xs-8">
                        <div class="report-item-author">
                          <div class="user-username " style="text-align: left">
                            <span class="user-level">订单生成时间 :{{item.create_time}}<br>流水号:{{item.code}}<br>订单号:{{item.order_sn}}<br></span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class=" report-item clearfix" style="text-align: left" v-for="item in courseOrders">
                      <div class="report-item-course" style="float: left">
                      </div>
                      <br>
                      <div class="tags" style="text-align: left">
                        <br>
                        <span class="tag"><h2>课程名:{{item.course_name}}</h2></span>
                        <br>
                        <span class="tag tag-primary">订单金额:{{item.pay_price}}</span>
                        <br>

                        <!--                        <span class="tag tag-primary" v-if="item.course_name!=''">课程名:{{item.pay_price}}</span>-->
                        <span class="tag tag-primary" v-if="item.pay_type==1">支付方式:支付宝</span>
                        <br>

                        <span class="tag tag-primary" v-if="item.num>0">使用的积分{{item.num}}</span>
                        <br>

                        <span class="tag tag-primary">优惠金额{{item.preferential_money}}</span>
                        <br>


                      </div>
                      <div class="col-xs-8">
                        <div class="report-item-author">
                          <div class="user-username " style="text-align: left">
                            <span class="user-level">订单生成时间 :{{item.create_time}}<br>流水号:{{item.code}}<br>订单号:{{item.order_number}}<br></span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div role="tabpanel" :class="{'tab-pane':true,'active':this.whatActive ==='SetUp'}">
                <div class="row">
                  <div class="row report-items" style="text-align: left">
                    <div class="" style="text-align: left">
                      <div class="col-xs-8">
                        <div class="report-item-author">
                          <div class="user-username " style="text-align: left">
                            <span class="user-level">修改头像<br></span>
                            <br>
                            <input type="file" class="" name="" id='img'>
                            <br>
                            <span class="user-level">修改密码<br></span>
                            <br>
                            <input type="password" v-model="password" class="form-control" placeholder="请输入原密码">
                            <br>
                            <input type="password" v-model="password1" class="form-control" placeholder="请输入新密码">
                            <br>
                            <input type="password" v-model="password2" class="form-control" placeholder="请输入确认密码">
                            <br>
                            <input class="btn btn-primary" name="submit" type="submit" value="提交" @click="submit">
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>


          <!---->
        </div>
        <!--      没毛病-->
        <div class="modal fade" id="modal-message" tabindex="-1" role="dialog" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span
                  class="sr-only">Close</span></button>
                <h4 class="modal-title">标题:{{item.title}}</h4>
              </div>
              <div class="modal-body">
                {{item.content}}
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                <button type="button" class="btn btn-primary confirm" data-dismiss="modal">确定</button>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-3 layout-side">
          <!---->
          <!---->
          <a class="side-sda apply-git" href="http://git.shiyanlou.com/shilei" target="_blank">
            <img src="../../static/img/my-git.png">
            <span>代码库</span>
          </a>
          <!---->
          <!---->
          <div class="sidebox user-visitors">
            <div class="sidebox-header">
              <h4 class="sidebox-title">最近来访</h4>
            </div>
            <div class="sidebox-body">
              <!---->
              <div class="col-dm-12">
                <a class="row" href="/user/345538">
                  <div class="col-xs-2">
                    <img
                      src="https://dn-simplecloud.shiyanlou.com/gravatar345538.png?v=1483141057082&amp;imageView2/1/w/200/h/200">
                  </div>
                  <div class="col-xs-10">
                    <div>PKU_Hao</div>
                    <div>12分钟前</div>
                  </div>
                </a>
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
    import {send, sendToken} from '../../static/js/comm'


    export default {
        name: "visitOther",
        data: function () {
            return {
                whatActive: 'Orders',
                coupons: [],
                myCoupons: [],
                userInfo: {},
                level_name: '',
                myOrders: [],
                courseOrders: [],
                myCouponID: [],
                clist: [],
                whatS: 'a',
                formdata: new FormData,
                password: '',
                password1: '',
                password2: '',
                user_id: localStorage.getItem('user_id'),
                myMessage: [],
                item: {},
                learnList: [],
            }
        },
        mounted() {
            sendToken('/api/user/?user_id=' + localStorage.getItem('user_id'), 'get').then((res) => {
                if (res.data.code == 200) {
                    this.userInfo = res.data.userInfo
                    this.level_name = this.userInfo.level.level_name
                    this.myCouponID = res.data.myCoupon
                } else {
                    alert(res.data.message)
                }
            });
            sendToken('/api/memberOrder/', 'put', {'user_id': localStorage.getItem('user_id')}).then((res) => {
                this.myOrders = res.data.dataList;
                this.courseOrders = res.data.courseOrders
            });
            this.axios.get('/api/uploadcourse/?user_id=' + localStorage.getItem('user_id')).then((res) => {
                if (res.data.code == 200) {
                    this.clist = res.data.courseList;
                    this.learnList = res.data.learnList


                }
            })
        },
        methods: {
            getIt: function (id) {
                send('/api/mycoupon/', 'post', {'user_id': this.userInfo.id, 'coupon_id': id}).then((res) => {
                    if (res.data.code == 200) {
                        this.showWhat('myCoupon')
                    } else {
                        alert(res.data.message)
                    }
                })

            },
            getUserInfo: function () {
            },
            getCoupon: function () {
                send('/api/admin01/coupon/', 'get').then((res) => {
                    if (res.data.code == 200) {
                        this.coupons = res.data.dataList
                    }
                })
            },
            getUserCoupon: function () {
                send('/api/mycoupon/?user_id=' + localStorage.getItem('user_id'), 'get').then((res) => {
                    if (res.data.code == 200) {
                        this.myCoupons = res.data.couponList
                    }
                })
            },
            getMyCourse: function () {
            },
            showWhat: function (n, m) {
                this.whatActive = n;
                this.whatS = m
                if (n == 'coupon') {
                    this.getCoupon()
                }
                if (n == 'myCoupon') {
                    this.getUserCoupon()
                }
                if (n == 'course') {
                }
                if (n == 'SiteMessage') {
                    send('/api/mySiteMessage/?user_id=' + localStorage.getItem('user_id')).then((res) => {
                        if (res.data.code == 200) {
                            this.myMessage = res.data.messageList
                        }
                    })
                }
            },
            submit: function () {
                // let formdata=new Formdata;
                this.formdata.append('file', document.getElementById('img').files[0])
                this.formdata.append('password', this.password);
                if (this.password1 == this.password2) {
                    this.formdata.append('password1', this.password);
                } else {
                    alert('确认密码错误')
                }
                sendToken('/api/user/?user_id=' + this.user_id, 'put', this.formdata).then((res) => {
                    alert('修改成功')
                    this.$router.push({path: 'userCenter'})
                })
            },
            showdetail: function (item) {
                $('#modal-message').modal('show')
                this.item = item
                send('/api/mySiteMessage/', 'post', {
                    'user_id': localStorage.getItem('user_id'),
                    'mid': item.id
                }).then((res) => {
                    if (res.data.code == 200) {
                        item.status = 1
                    }
                })
            }

        },
        components: {
            header1: header1,
            footer1: footer1
        },
    }
</script>

<style scoped>

</style>

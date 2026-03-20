// ================= REPORT =================
function submitReport(){

let data={
description:document.getElementById("problemDesc").value,
location:document.getElementById("problemLocation").value,
category:document.getElementById("problemCategory").value
};

fetch("/submit_report",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})
.then(res=>res.json())
.then(data=>{
alert("Tracking ID: "+data.id);
});
}

// ================= TRACK =================
function trackComplaint(){

let id=document.getElementById("trackInput").value;

fetch("/track_report/"+id)
.then(res=>res.json())
.then(data=>{

let div=document.getElementById("trackResult");

if(data.error){
div.innerHTML="Not Found";
}else{
div.innerHTML=`
<p>ID: ${data.id}</p>
<p>Status: ${data.status}</p>
<p>${data.description}</p>
`;
}
});
}

// ================= ADMIN =================
function loadAdmin(){

fetch("/all_reports")
.then(res=>res.json())
.then(data=>{

let div=document.getElementById("adminReportsList");
div.innerHTML="";

data.forEach(r=>{
div.innerHTML+=`
<div>
<p>${r[0]} - ${r[4]}</p>
<select onchange="updateStatus('${r[0]}',this.value)">
<option>Pending</option>
<option>In Progress</option>
<option>Resolved</option>
</select>
</div>
`;
});
});
}

function updateStatus(id,status){

fetch("/update_status",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({id,status})
})
.then(()=>loadAdmin());
}


setInterval(()=>{
  loadAnalytics();   // or loadAdminDashboard()
},5000);


function animateCounter(id, target){
  let count = 0;
  let interval = setInterval(()=>{
    count++;
    document.getElementById(id).innerText = count;
    if(count >= target) clearInterval(interval);
  },20);
}

animateCounter("counter1", 120);
animateCounter("counter2", 85);
animateCounter("counter3", 12);
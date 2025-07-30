const i = [10, 22, 32, 4, 15, 25, 17, 42, 52, 62, 72, 82];

	const hashArray = new Array(i.length - 1);
	
	const hasfFun = (val) => {
	  return val % 10;
	};
	
	const insert = () => {
	  console.log("ABOVE INSERT FOR LOOP");
	  for (let x = 0; x <= i.length - 1; x++) {
    console.log("INSIDE FOR LOOP");
	    let index = hasfFun(i[x]);
		    if (hashArray[index] === undefined) {
          hashArray[index] = i[x];
	    } else {
	      console.log("inside the else");
	      while (hashArray[index] != undefined) {
	        const len = i.length - 1
	        if(index == len) index = 0
       
            index += 1;
	      }
          hashArray[index] = i[x];
	    }
	  }
	};
	
	const find = (val) => {
	  let index = hasfFun(val);
	
	  if (hashArray[index] == val) return `THe ${val} is preset at ${index}`;
		  while (hashArray[index + 1] != val) {
	    index += 1;
	    const len = i.length - 1;
	    if (index === len) index = 0;
	  }
	  return `THe ${val} is preset at ${index}`;
	};
	
	insert();
	
	console.log("🚀 -------------------------🚀");
	console.log("🚀 ~ hashArray:", hashArray);
	console.log("🚀 -------------------------🚀");
	
	console.log(find(32));
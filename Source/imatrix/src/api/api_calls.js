const origin = "localhost:5000";
const upload_endpoint = "upload"

const postImage = (postData) => {

    var headers = new Headers();
    headers.append('Content-Type', 'multipart/form-data');


    const req = new Request(`http://${origin}/${upload_endpoint}/`, {
        method: 'POST',
        headers: headers,
        data: postData,
    });

    return returnData(req);
}

const returnData = req => (
    fetch(req).then(res =>
        res.json().then(data =>
            data
        )
    )
);


export { postImage };
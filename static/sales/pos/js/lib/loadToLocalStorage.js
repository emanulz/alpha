
//LOCAL STORAGE FUNCTIONS
//------------------------------------------------------------------------------------------
export function loadToLocalStorage(store){

    localStorage.Products=null;
    localStorage.Clients=null;
    productsToMemory(store);
    clientsToMemory(store);

}//MAIN SAVE TO LOCAL STORAGE

function productsToMemory(store) {

    $.get(`/sales/api/products/?company=${store.companyId}`, function (data) {

    }).success((data)=> {
        localStorage.Products=JSON.stringify(data);
    });

}//SAVE PRODUCTS TO LOCAL STORAGE

function clientsToMemory(store) {

    $.get(`/sales/api/clients/?company=${store.companyId}`, function (data) {

    }).success((data)=>{
         localStorage.Clients=JSON.stringify(data);
    });

}//SAVE CLIENTS TO LOCAL STORAGE
//------------------------------------------------------------------------------------------

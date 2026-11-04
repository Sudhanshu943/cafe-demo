export const menu={
 coffee:[{name:'Flat White',detail:'Double espresso, silky steamed milk',price:240,image:'latte'},{name:'Honey Oat Latte',detail:'Espresso, oat milk, a little honey',price:280,image:'coffee'},{name:'Cold Brew',detail:'Slow-steeped coffee, served over ice',price:260,image:'iced'},{name:'Espresso',detail:'A small cup with a lot to say',price:180,image:'espresso'}],
 matcha:[{name:'Ceremonial Matcha',detail:'Whisked matcha, warm or over ice',price:280,image:'matcha'},{name:'Iced Matcha Latte',detail:'Matcha and milk, softly balanced',price:300,image:'matcha'},{name:'Oat Matcha',detail:'Whisked matcha with oat milk',price:320,image:'matcha'}],
 kitchen:[{name:'Butter Croissant',detail:'Golden layers, baked for slow mornings',price:190,image:'pastry'},{name:'Avocado Toast',detail:'Sourdough, avocado, lemon and seeds',price:340,image:'brunch'},{name:'Cinnamon Bun',detail:'Soft dough, cinnamon, vanilla glaze',price:220,image:'bread'}]
};
export const money=n=>new Intl.NumberFormat('en-IN',{style:'currency',currency:'INR',maximumFractionDigits:0}).format(n);
